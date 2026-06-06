from __future__ import annotations

from collections.abc import Sequence
from typing import TypeVar

T = TypeVar("T")


def build_double_round_robin(entries: Sequence[T]) -> list[tuple[T, T]]:
    """Return every two-player pairing twice, swapping player order."""
    schedule: list[tuple[T, T]] = []
    for first_index in range(len(entries)):
        for second_index in range(first_index + 1, len(entries)):
            first = entries[first_index]
            second = entries[second_index]
            schedule.append((first, second))
            schedule.append((second, first))
    return schedule


def double_round_robin_match_count(participant_count: int) -> int:
    if participant_count < 2:
        return 0
    return participant_count * (participant_count - 1)
