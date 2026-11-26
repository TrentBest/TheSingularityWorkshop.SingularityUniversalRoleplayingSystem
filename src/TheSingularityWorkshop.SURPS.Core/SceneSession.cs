namespace TheSingularityWorkshop.SURPS.Core;

public sealed record SceneEntity(string Id, string Name, string ParentId, IReadOnlySet<string> AvailableActionIds, bool IsPlayerVisible = true);
public sealed record SceneActor(string Id, string InventoryContainerId, IReadOnlySet<string> Capabilities);
public sealed record SceneAction(string Id, string RequiredCapability, bool RequiresReferee = true);

public enum IntentStatus { PendingAdjudication, Committed, Rejected, Stale }

public sealed record SceneIntent(Guid Id, string ActorId, string EntityId, string ActionId, string? DestinationEntityId,
    long ExpectedRevision, IntentStatus Status, string? DecisionReason = null);
public sealed record ObservedEntity(string Id, string Name, string ParentId, IReadOnlyList<string> AvailableActions);
public sealed record SceneProjection(long Revision, string ObserverId, IReadOnlyList<ObservedEntity> Entities);
public sealed record IntentResult(SceneIntent Intent, long CurrentRevision);

/// <summary>
/// Minimal authoritative scene aggregate. Renderers receive projections and adapters submit proposals;
/// neither receives a mutation API. Durable storage and transport remain host responsibilities.
/// </summary>
public sealed class SceneSession
{
    private readonly Dictionary<string, SceneEntity> _entities;
    private readonly Dictionary<string, SceneActor> _actors;
    private readonly Dictionary<string, SceneAction> _actions;
    private readonly Dictionary<Guid, SceneIntent> _intents = [];

    public SceneSession(IEnumerable<SceneEntity> entities, IEnumerable<SceneActor> actors,
        IEnumerable<SceneAction> actions, long initialRevision = 0)
    {
        if (initialRevision < 0) throw new ArgumentOutOfRangeException(nameof(initialRevision));
        _entities = UniqueById(entities, x => x.Id, nameof(entities));
        _actors = UniqueById(actors, x => x.Id, nameof(actors));
        _actions = UniqueById(actions, x => x.Id, nameof(actions));
        Revision = initialRevision;
        foreach (var entity in _entities.Values)
        {
            if (!_entities.ContainsKey(entity.ParentId))
                throw new ArgumentException($"Entity '{entity.Id}' references missing parent '{entity.ParentId}'.", nameof(entities));
            foreach (var actionId in entity.AvailableActionIds)
                if (!_actions.ContainsKey(actionId))
                    throw new ArgumentException($"Entity '{entity.Id}' references unknown action '{actionId}'.", nameof(entities));
        }
        foreach (var actor in _actors.Values)
            if (!_entities.ContainsKey(actor.InventoryContainerId))
                throw new ArgumentException($"Actor '{actor.Id}' references missing inventory container.", nameof(actors));
    }

    public long Revision { get; private set; }
    public IReadOnlyCollection<SceneIntent> Intents => _intents.Values.ToArray();

    /// <summary>Creates an observer-scoped projection; non-player-visible entities are omitted.</summary>
    public SceneProjection Observe(string actorId)
    {
        if (!_actors.TryGetValue(actorId, out var actor)) throw new KeyNotFoundException($"Unknown actor '{actorId}'.");
        var visible = _entities.Values.Where(x => x.IsPlayerVisible).Select(entity =>
        {
            var permitted = entity.AvailableActionIds
                .Where(id => _actions.TryGetValue(id, out var action) &&
                    (action.RequiredCapability.Length == 0 || actor.Capabilities.Contains(action.RequiredCapability)))
                .Order(StringComparer.Ordinal).ToArray();
            return new ObservedEntity(entity.Id, entity.Name, entity.ParentId, permitted);
        }).ToArray();
        return new SceneProjection(Revision, actorId, visible);
    }

    /// <summary>Records a proposal only. No world state changes until adjudication.</summary>
    public IntentResult Propose(Guid intentId, string actorId, string entityId, string actionId,
        long expectedRevision, string? destinationEntityId = null)
    {
        if (intentId == Guid.Empty) throw new ArgumentException("Intent identity must be non-empty.", nameof(intentId));
        if (_intents.ContainsKey(intentId)) throw new InvalidOperationException($"Intent '{intentId}' already exists.");
        if (expectedRevision != Revision)
            return Record(intentId, actorId, entityId, actionId, destinationEntityId, expectedRevision, IntentStatus.Stale, "Scene revision changed.");
        if (!_actors.TryGetValue(actorId, out var actor))
            return Record(intentId, actorId, entityId, actionId, destinationEntityId, expectedRevision, IntentStatus.Rejected, "Unknown actor.");
        if (!_entities.TryGetValue(entityId, out var entity) || !entity.IsPlayerVisible)
            return Record(intentId, actorId, entityId, actionId, destinationEntityId, expectedRevision, IntentStatus.Rejected, "Entity is unavailable to this participant.");
        if (!_actions.TryGetValue(actionId, out var action) || !entity.AvailableActionIds.Contains(actionId))
            return Record(intentId, actorId, entityId, actionId, destinationEntityId, expectedRevision, IntentStatus.Rejected, "Action is not available for this entity.");
        if (action.RequiredCapability.Length > 0 && !actor.Capabilities.Contains(action.RequiredCapability))
            return Record(intentId, actorId, entityId, actionId, destinationEntityId, expectedRevision, IntentStatus.Rejected, "Actor lacks the required capability.");
        if (actionId == "take" && (destinationEntityId != actor.InventoryContainerId || !_entities.ContainsKey(destinationEntityId)))
            return Record(intentId, actorId, entityId, actionId, destinationEntityId, expectedRevision, IntentStatus.Rejected, "Taking must target the actor's own inventory container.");
        return Record(intentId, actorId, entityId, actionId, destinationEntityId, expectedRevision,
            IntentStatus.PendingAdjudication, action.RequiresReferee ? null : "Automatic resolution is not enabled in this proof.");
    }

    /// <summary>Adjudicates against the exact revision on which the proposal was made.</summary>
    public IntentResult Adjudicate(Guid intentId, bool accepted, string adjudicatorId, string reason)
    {
        if (string.IsNullOrWhiteSpace(adjudicatorId)) throw new ArgumentException("Adjudicator identity is required.", nameof(adjudicatorId));
        if (string.IsNullOrWhiteSpace(reason)) throw new ArgumentException("A decision reason is required.", nameof(reason));
        if (!_intents.TryGetValue(intentId, out var intent)) throw new KeyNotFoundException($"Unknown intent '{intentId}'.");
        if (intent.Status != IntentStatus.PendingAdjudication) throw new InvalidOperationException("Only pending intents may be adjudicated.");
        if (intent.ExpectedRevision != Revision)
            return Replace(intent with { Status = IntentStatus.Stale, DecisionReason = "Scene revision changed before adjudication." });
        if (!accepted) return Replace(intent with { Status = IntentStatus.Rejected, DecisionReason = reason });
        if (intent.ActionId == "take")
        {
            var entity = _entities[intent.EntityId];
            _entities[entity.Id] = entity with { ParentId = intent.DestinationEntityId! };
        }
        Revision++;
        return Replace(intent with { Status = IntentStatus.Committed, DecisionReason = reason });
    }

    private IntentResult Record(Guid id, string actor, string entity, string action, string? destination,
        long expected, IntentStatus status, string? reason)
    {
        var intent = new SceneIntent(id, actor, entity, action, destination, expected, status, reason);
        _intents.Add(id, intent);
        return new IntentResult(intent, Revision);
    }

    private IntentResult Replace(SceneIntent intent)
    {
        _intents[intent.Id] = intent;
        return new IntentResult(intent, Revision);
    }

    private static Dictionary<string, T> UniqueById<T>(IEnumerable<T> items, Func<T, string> id, string parameter)
    {
        ArgumentNullException.ThrowIfNull(items);
        var result = new Dictionary<string, T>(StringComparer.Ordinal);
        foreach (var item in items)
        {
            var key = id(item);
            if (string.IsNullOrWhiteSpace(key)) throw new ArgumentException("IDs must be non-empty.", parameter);
            if (!result.TryAdd(key, item)) throw new ArgumentException($"Duplicate ID '{key}'.", parameter);
        }
        return result;
    }
}