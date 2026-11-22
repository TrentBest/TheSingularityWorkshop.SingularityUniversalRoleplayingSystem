using TheSingularityWorkshop.MicroBundleDomain;

namespace TheSingularityWorkshop.SingularityUniversalRoleplayingSystem.Rulebooks;

/// <summary>
/// Stable identity for the SURPS Dungeons and Underground rulebook container.
/// </summary>
public static class SurpsRulebookDungeonsAndUndergroundIdentity
{
    public const string CanonicalId =
        "TheSingularityWorkshop.SingularityUniversalRoleplayingSystem.SurpsRulebookDungeonsAndUnderground";

    // FNV-1a 64-bit hash of CanonicalId.
    public const ulong Id = 0x62F30CCED4164D40UL;
}

/// <summary>
/// Stable identity of the underlying FSM_Dungeon environment MicroBundle.
/// </summary>
public static class DungeonEnvironmentDependency
{
    public const string CanonicalId = "TheSingularityWorkshop.FSM_Dungeon";

    // Must match DungeonMicroBundleIdentity.Id in FSM_Dungeon.
    public const ulong BundleId = 0xC0C3B15E31815313UL;
}

/// <summary>
/// Presents the FSM_Dungeon underground-environment capability as a SURPS rulebook.
/// </summary>
/// <remarks>
/// This is a composition wrapper, not a second dungeon implementation. Its dependency
/// request causes the composition host to resolve the authoritative Dungeon MicroBundle.
/// SURPS owns the rulebook presentation boundary; FSM_Dungeon remains authoritative for
/// underground environments. The current rulebook contract is a marker and does not yet
/// claim a finalized ontology/rule serialization format.
/// </remarks>
public sealed class SurpsRulebookDungeonsAndUnderground : ISurpsRulebook
{
    public MicroBundleDescriptor Descriptor { get; } = new(
        SurpsRulebookDungeonsAndUndergroundIdentity.Id,
        "0.1.0-alpha.1",
        dependencies:
        [
            new MicroBundleDependency(DungeonEnvironmentDependency.BundleId)
        ],
        providers:
        [
            new MicroBundleProvider("surps.rulebook.dungeons-and-underground")
        ]);

    public IReadOnlyList<MicroBundleDependencyRequest> Dependencies { get; } =
    [
        MicroBundleDependencyRequest.Unconfigured(DungeonEnvironmentDependency.BundleId)
    ];

    public void Load(IMicroBundleLoadContext context)
    {
        ArgumentNullException.ThrowIfNull(context);
    }

    public bool Arbitrate(IMicroBundleArbitrationContext context, int roundIndex)
    {
        ArgumentNullException.ThrowIfNull(context);
        ArgumentOutOfRangeException.ThrowIfNegative(roundIndex);
        return false;
    }
}
