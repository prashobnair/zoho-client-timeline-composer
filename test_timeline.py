import json
import unittest
from pathlib import Path
from timeline import compose, parse_time

EVENTS = json.loads(Path(__file__).with_name('examples.json').read_text())['events']

class TimelineTests(unittest.TestCase):
    def test_internal_conflict_and_order(self):
        result = compose(EVENTS)
        self.assertEqual(4, result['visible_count'])
        self.assertEqual(['call-1','email-1','deal-1','milestone-1'], [e['id'] for e in result['timeline']])
        self.assertEqual(['call-1','email-1'], result['conflicts'][0]['event_ids'])

    def test_client_filters_before_conflict(self):
        result = compose(EVENTS, 'client')
        self.assertEqual(['call-1','deal-1'], [e['id'] for e in result['timeline']])
        self.assertEqual([], result['conflicts'])
        text = str(result)
        self.assertNotIn('2026-02-15', text)
        self.assertNotIn('Internal delivery review', text)

    def test_same_instant_normalization(self):
        self.assertEqual(parse_time('2026-01-05T10:00:00+05:30'), parse_time('2026-01-05T04:30:00Z'))

    def test_naive_time_rejected(self):
        with self.assertRaises(ValueError):
            parse_time('2026-01-05T10:00:00')

    def test_duplicate_id_rejected(self):
        with self.assertRaises(ValueError):
            compose([EVENTS[0], EVENTS[0]])

    def test_bad_visibility_rejected(self):
        with self.assertRaises(ValueError):
            compose([dict(EVENTS[0], visibility='public')])

if __name__ == '__main__':
    unittest.main()
