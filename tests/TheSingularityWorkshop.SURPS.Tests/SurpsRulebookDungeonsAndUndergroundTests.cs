using Xunit;
using TheSingularityWorkshop.MicroBundleDomain;
using TheSingularityWorkshop.SingularityUniversalRoleplayingSystem;
using TheSingularityWorkshop.SingularityUniversalRoleplayingSystem.Rulebooks;

namespace TheSingularityWorkshop.SURPS.Tests;

public sealed class SurpsRulebookDungeonsAndUndergroundTests
{
    [Fact]
    public void Rulebook_IsASurpsRulebookMicroBundle()
    {
        var rulebook = new SurpsRulebookDungeonsAndUnderground();

        Assert.IsAssignableFrom<ISurpsRulebook>(rulebook);
        Assert.Equal(SurpsRulebookDungeonsAndUndergroundIdentity.Id, rulebook.Descriptor.Id);
        Assert.Contains(rulebook.Descriptor.Providers,
            provider => provider.Id == "surps.rulebook.dungeons-and-underground");
    }

    [Fact]
    public void Rulebook_DeclaresDungeonAsItsRequiredDomainMicroBundle()
    {
        var rulebook = new SurpsRulebookDungeonsAndUnderground();

        Assert.Contains(rulebook.Descriptor.Dependencies,
            dependency => dependency.BundleId == DungeonEnvironmentDependency.BundleId);
        Assert.Contains(rulebook.Dependencies,
            dependency => dependency.BundleId == DungeonEnvironmentDependency.BundleId);
        Assert.Single(rulebook.Dependencies);
    }

    [Fact]
    public void Rulebook_DoesNotDuplicateDungeonImplementationOrAddOtherDomainDependencies()
    {
        var rulebook = new SurpsRulebookDungeonsAndUnderground();

        Assert.Single(rulebook.Descriptor.Dependencies);
        Assert.Equal(DungeonEnvironmentDependency.CanonicalId, "TheSingularityWorkshop.FSM_Dungeon");
    }

    [Fact]
    public void Rulebook_LoadAndArbitrationRemainHostNeutral()
    {
        var rulebook = new SurpsRulebookDungeonsAndUnderground();

        rulebook.Load(new TestLoadContext());
        Assert.False(rulebook.Arbitrate(new TestArbitrationContext(), 0));
    }

    private sealed class TestLoadContext : IMicroBundleLoadContext
    {
        public ulong RuntimeId => 1;

        public bool TryGetConfiguration(ulong bundleId, out ReadOnlyMemory<byte> configuration)
        {
            configuration = ReadOnlyMemory<byte>.Empty;
            return false;
        }
    }

    private sealed class TestArbitrationContext : IMicroBundleArbitrationContext
    {
        public ulong RuntimeId => 1;
        public IReadOnlyList<IMicroBundle> Bundles => Array.Empty<IMicroBundle>();
        public object? ExperienceContext => null;
    }
}
