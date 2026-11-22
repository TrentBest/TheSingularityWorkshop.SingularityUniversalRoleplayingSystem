using TheSingularityWorkshop.MicroBundleDomain;

namespace TheSingularityWorkshop.SingularityUniversalRoleplayingSystem;

/// <summary>
/// Marks a MicroBundle that presents domain knowledge through the SURPS rulebook layer.
/// </summary>
/// <remarks>
/// This first contract is intentionally minimal. Rulebook metadata, ontology contributions,
/// structured rules, and source-book references will be added after the same contract has
/// been validated against multiple domain integrations (beginning with Physics and Laboratories).
/// </remarks>
public interface ISurpsRulebook : IMicroBundle
{
}
