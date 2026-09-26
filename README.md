# Zoho Client Timeline Composer

An offline composer for a fictional client's calls, email *references*, deals and project milestones. It keeps source IDs with each event, sorts timezone-aware dates and flags contradictory claims for review. It has a separate internal/client view and filters internal records before producing client-facing conflict details. It does not read actual email, fetch CRM records or send a timeline to anyone.

## Contract use-case

The [Zoho CRM contract board](https://www.upwork.com/freelance-jobs/zoho-crm/) sampled a client-history CRM configuration request, from first call onward. A [setup/cleanup brief](https://www.freelancer.com/projects/zoho-crm/zoho-crm-setup-cleanup) asks for data and custom-field organization. This prototype isolates the provenance and conflict-review slice, not a production CRM configuration or work for either poster.

## Run

Python 3.10+ and standard library only. From the repo root:

```sh
python3 cli.py examples.json
python3 cli.py examples.json --audience client
python3 -m unittest discover -p 'test_*.py' -v
```

No Zoho trial, inbox connection, API key, Docker or paid plan is needed. The fictional sample has four events. Internal view shows four events and a launch-date conflict between a call and an internal email reference; client view shows only two permitted events and no disclosure of the internal claim. The CLI only prints local JSON. `DESIGN.md` covers provenance, permissions, tests and review.

## Data contract

Every event needs unique `id`, a `type` (`call`, `email_reference`, `deal`, `milestone`), timezone-aware ISO `at`, `source_id`, `summary` and `visibility` (`internal`/`client`). Optional `claim` has key/value. Conflicts arise when visible events make different values for the same key. The tool does **not** choose which one is right; a person must review source records and audience restrictions. Source IDs are fictional opaque references, not valid Zoho IDs or retrievable links.

## Safety boundary

Real clients may have audience-specific restrictions narrower than this two-level demo. A caller's statement, an email, or a deal stage may be stale or wrong. Never assume a timestamp or a last-write wins rule establishes truth. Before connecting to a real tenant, inspect current API metadata, permission model, content retention and source ownership, and test redaction and authorization on actual roles. Do not import employer, customer or real email data into this repository.
