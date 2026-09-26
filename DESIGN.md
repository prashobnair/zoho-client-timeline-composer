# Provenance and access design

## Workflow

The sample has four fictional sources and no external data connectors. A real implementation would ingest only approved sources, preserve immutable IDs and timestamps, record source-specific access restrictions, and make the original record reachable only by authorized staff. It would distinguish event occurrence time from record creation/update time. Conflicts need a reviewer who can inspect both originals and document the resolution; a composer must not silently pick the latest claim.

## Audience model

This prototype's `client` view includes only entries explicitly labeled `client`. It filters *before* conflict calculation to avoid leaking an internal claim through a finding. It is not a complete authorization system: event labels here are trusted fixture metadata, whereas real systems require authenticated permissions, tenant boundaries and field-level controls. Do not expose internal source IDs in a public link. No user-facing message is sent by this program.

## Tests and limits

Six tests cover ordering, conflicting claims, audience filtering, equivalent timezone instants, naive timestamps, duplicate IDs and unsupported visibility. Missing: redaction of summaries, updates/deletions, source-authentication, cross-client isolation, field-level policy, time-zone display preferences and live CRM API contract tests. These gaps are deliberate and must be addressed before production use.
