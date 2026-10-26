"""Student decision policy for the course-local Line Arena.

Week 14 principle: prefer composition. Bot receives a strategy callable instead
of hardcoding one policy inside the class.
"""

from collections.abc import Callable

State = dict[str, int]
Strategy = Callable[[State], str]


def move_toward_goal(state: State) -> str:
    """Return a legal local action that moves toward the goal when possible."""
    position = state.get("position")
    goal = state.get("goal")
    if (
        not isinstance(position, int)
        or isinstance(position, bool)
        or not isinstance(goal, int)
        or isinstance(goal, bool)
    ):
        return "wait"
    if position < goal:
        return "right"
    if position > goal:
        return "left"
    return "wait"


def balanced_strategy(state: State) -> str:
    """Use the straightforward policy: move toward the goal."""
    return move_toward_goal(state)


def defensive_strategy(state: State) -> str:
    """Wait when the opponent is adjacent; otherwise move toward the goal."""
    position = state.get("position")
    opponent_position = state.get("opponent_position")
    if (
        isinstance(position, int)
        and not isinstance(position, bool)
        and isinstance(opponent_position, int)
        and not isinstance(opponent_position, bool)
        and abs(opponent_position - position) <= 1
    ):
        return "wait"
    return move_toward_goal(state)


def aggressive_strategy(state: State) -> str:
    """Prioritize progress toward the goal on every non-terminal position.

    The course-local arena has no attack action, so "aggressive" means it does
    not pause just because the opponent is nearby.
    """
    return move_toward_goal(state)


class Bot:
    """A bot that delegates its decision to a replaceable strategy."""

    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def choose_action(self, state: State) -> str:
        """Delegate the decision; the arena-facing function stays unchanged."""
        return self.strategy(state)


# Keep the arena's existing function interface stable.
_DEFAULT_BOT = Bot(balanced_strategy)


def choose_action(state: State) -> str:
    """Choose a course-local action; invalid or incomplete state returns wait."""
    return _DEFAULT_BOT.choose_action(state)


def main() -> None:
    """Run a small example of the default decision policy."""
    state = {
        "turn": 1,
        "max_turns": 6,
        "position": 0,
        "opponent_position": 4,
        "goal": 4,
        "min_position": 0,
        "max_position": 4,
    }
    print(choose_action(state))


if __name__ == "__main__":
    main()
