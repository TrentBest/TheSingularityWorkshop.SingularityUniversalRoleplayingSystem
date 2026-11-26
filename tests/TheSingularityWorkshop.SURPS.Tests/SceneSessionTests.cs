using TheSingularityWorkshop.SURPS.Core;
using Xunit;

namespace TheSingularityWorkshop.SURPS.Tests;

public sealed class SceneSessionTests
{
    private static SceneSession CreateSession() => new(
        [
            new SceneEntity("world", "World", "world", new HashSet<string>(), false),
            new SceneEntity("room", "Room", "world", new HashSet<string>()),
            new SceneEntity("counter", "Counter", "room", new HashSet<string>()),
            new SceneEntity("inventory", "Player inventory", "room", new HashSet<string>(), false),
            new SceneEntity("knife", "Knife", "counter", new HashSet<string> { "inspect", "take" })
        ],
        [new SceneActor("player", "inventory", new HashSet<string> { "manipulate" })],
        [new SceneAction("inspect", "", true), new SceneAction("take", "manipulate", true)]);

    [Fact]
    public void ProjectionOmitsHiddenEntitiesAndFiltersActionsByCapability()
    {
        var projection = CreateSession().Observe("player");
        Assert.DoesNotContain(projection.Entities, x => x.Id == "inventory");
        Assert.DoesNotContain(projection.Entities, x => x.Id == "world");
        Assert.Contains("take", projection.Entities.Single(x => x.Id == "knife").AvailableActions);
    }

    [Fact]
    public void ProposalDoesNotMutateAndAcceptedTakePreservesIdentity()
    {
        var session = CreateSession();
        var intent = session.Propose(Guid.NewGuid(), "player", "knife", "take", session.Revision, "inventory").Intent;
        Assert.Equal(IntentStatus.PendingAdjudication, intent.Status);
        Assert.Equal("counter", session.Observe("player").Entities.Single(x => x.Id == "knife").ParentId);
        Assert.Equal(0, session.Revision);

        var result = session.Adjudicate(intent.Id, true, "referee", "The player can reach and lift the knife.");
        Assert.Equal(IntentStatus.Committed, result.Intent.Status);
        Assert.Equal(1, session.Revision);
        var moved = session.Observe("player").Entities.Single(x => x.Id == "knife");
        Assert.Equal("knife", moved.Id);
        Assert.Equal("inventory", moved.ParentId);
    }

    [Fact]
    public void StaleProposalAndStaleAdjudicationFailClosed()
    {
        var session = CreateSession();
        Assert.Equal(IntentStatus.Stale, session.Propose(Guid.NewGuid(), "player", "knife", "take", 99, "inventory").Intent.Status);
        var pending = session.Propose(Guid.NewGuid(), "player", "knife", "take", 0, "inventory").Intent;
        session.Adjudicate(pending.Id, false, "referee", "Scenario disallows it.");
        var oldRevisionIntent = session.Propose(Guid.NewGuid(), "player", "knife", "take", session.Revision, "inventory").Intent;
        var advancingIntent = session.Propose(Guid.NewGuid(), "player", "knife", "take", session.Revision, "inventory").Intent;
        session.Adjudicate(advancingIntent.Id, true, "referee", "Accepted.");
        Assert.Equal(IntentStatus.Stale, session.Adjudicate(oldRevisionIntent.Id, true, "referee", "Too late.").Intent.Status);
    }

    [Fact]
    public void UnauthorizedActionIsRejectedWithoutChangingRevision()
    {
        var session = new SceneSession(
            [new SceneEntity("room", "Room", "room", new HashSet<string> { "take" })],
            [new SceneActor("visitor", "room", new HashSet<string>())],
            [new SceneAction("take", "manipulate")]);
        var result = session.Propose(Guid.NewGuid(), "visitor", "room", "take", 0, "room");
        Assert.Equal(IntentStatus.Rejected, result.Intent.Status);
        Assert.Equal(0, session.Revision);
    }
}