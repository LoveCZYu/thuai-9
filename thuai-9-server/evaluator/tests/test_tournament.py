from __future__ import annotations

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from tournament import build_double_round_robin, double_round_robin_match_count


class DoubleRoundRobinTests(unittest.TestCase):
    def test_builds_each_pair_twice_with_swapped_order(self) -> None:
        schedule = build_double_round_robin(["a", "b", "c"])

        self.assertEqual(
            [
                ("a", "b"),
                ("b", "a"),
                ("a", "c"),
                ("c", "a"),
                ("b", "c"),
                ("c", "b"),
            ],
            schedule,
        )

    def test_never_schedules_self_matches(self) -> None:
        schedule = build_double_round_robin([1, 2, 3, 4])

        self.assertEqual(12, len(schedule))
        self.assertTrue(all(first != second for first, second in schedule))

    def test_match_count(self) -> None:
        self.assertEqual(0, double_round_robin_match_count(0))
        self.assertEqual(0, double_round_robin_match_count(1))
        self.assertEqual(2, double_round_robin_match_count(2))
        self.assertEqual(6, double_round_robin_match_count(3))
        self.assertEqual(12, double_round_robin_match_count(4))


if __name__ == "__main__":
    unittest.main()
