"""Offline, fictional CRM client timeline; no email or Zoho access."""
from __future__ import annotations
from collections import defaultdict
from datetime import datetime, timezone

TYPES = {'call', 'email_reference', 'deal', 'milestone'}


def parse_time(value):
    if not isinstance(value, str):
        raise ValueError('timestamp must be ISO-8601 string with timezone')
    try:
        dt = datetime.fromisoformat(value.replace('Z', '+00:00'))
    except ValueError as exc:
        raise ValueError('invalid timestamp') from exc
    if dt.tzinfo is None or dt.utcoffset() is None:
        raise ValueError('naive timestamp is not allowed')
    return dt.astimezone(timezone.utc)


def compose(events, audience='internal'):
    if not isinstance(events, list) or audience not in {'internal', 'client'}:
        raise ValueError('events must be list and audience internal/client')
    ids = set()
    normalized = []
    conflicts = []
    claims = defaultdict(list)
    for row in events:
        if not isinstance(row, dict):
            raise ValueError('event must be object')
        eid = str(row.get('id', '')).strip()
        if not eid or eid in ids:
            raise ValueError('event IDs must be unique and nonempty')
        ids.add(eid)
        kind = row.get('type')
        if kind not in TYPES:
            raise ValueError('unsupported event type')
        if not isinstance(row.get('source_id'), str) or not row['source_id']:
            raise ValueError('each event needs source_id')
        if row.get('visibility') not in {'internal', 'client'}:
            raise ValueError('visibility must be internal/client')
        if not isinstance(row.get('summary'), str):
            raise ValueError('summary must be text')
        when = parse_time(row.get('at'))
        entry = {'id':eid,'type':kind,'at':when.isoformat(), 'summary':row['summary'],
                 'source_id':row['source_id'], 'visibility':row['visibility']}
        if audience == 'internal' or row['visibility'] == 'client':
            normalized.append(entry)
            claim = row.get('claim')
            if isinstance(claim, dict) and isinstance(claim.get('key'), str):
                claims[claim['key']].append((eid, str(claim.get('value', ''))))
    for key, values in sorted(claims.items()):
        if len({v for _, v in values}) > 1:
            conflicts.append({'key':key,'event_ids':[eid for eid, _ in values],
                              'code':'conflicting_claims'})
    normalized.sort(key=lambda r: (r['at'], r['id']))
    return {'audience':audience,'timeline':normalized,'conflicts':conflicts,
            'source_count':len(events),'visible_count':len(normalized)}
