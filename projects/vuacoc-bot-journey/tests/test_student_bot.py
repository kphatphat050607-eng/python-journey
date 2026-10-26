"""Behavior tests for the Week 15 student decision policy and W14 composition."""

import pytest

from local_arena.arena import LOCAL_ACTIONS
from student_bot.bot import (
    Bot,
    aggressive_strategy,
    balanced_strategy,
    choose_action,
    defensive_strategy,
)


@pytest.mark.parametrize(
    ("position", "goal", "expected"),
    [
        (0, 4, "right"),
        (1, 4, "right"),
        (3, 4, "right"),
        (4, 0, "left"),
        (3, 0, "left"),
        (1, 0, "left"),
        (0, 0, "wait"),
        (4, 4, "wait"),
    ],
)
def test_bot_moves_toward_goal(position, goal, expected):
    state = {"position": position, "goal": goal}
    assert choose_action(state) == expected


def test_bot_always_returns_a_legal_local_action():
    state = {
        "turn": 1,
        "max_turns": 6,
        "position": 2,
        "opponent_position": 3,
        "goal": 4,
        "min_position": 0,
        "max_position": 4,
    }
    assert choose_action(state) in LOCAL_ACTIONS


def test_bot_handles_missing_or_invalid_state_conservatively():
    assert choose_action({}) == "wait"
    assert choose_action({"position": "two", "goal": 4}) == "wait"
    assert choose_action({"position": True, "goal": 4}) == "wait"


def test_bot_is_deterministic_for_the_same_state():
    state = {"position": 1, "goal": 4}
    assert choose_action(state) == choose_action(state) == "right"


def test_composition_allows_strategy_to_be_injected():
    state = {"position": 1, "goal": 4}
    bot = Bot(strategy=lambda current_state: "wait")
    assert bot.choose_action(state) == "wait"


def test_defensive_strategy_waits_when_opponent_is_adjacent():
    state = {"position": 2, "opponent_position": 3, "goal": 4}
    assert defensive_strategy(state) == "wait"


def test_balanced_and_aggressive_strategies_move_toward_goal():
    state = {"position": 1, "opponent_position": 2, "goal": 4}
    assert balanced_strategy(state) == "right"
    assert aggressive_strategy(state) == "right"


def test_default_strategy_and_injected_strategy_can_differ():
    state = {"position": 2, "opponent_position": 3, "goal": 4}
    assert choose_action(state) == "right"
    assert Bot(defensive_strategy).choose_action(state) == "wait"
