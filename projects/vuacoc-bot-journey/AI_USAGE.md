# AI Usage Disclosure

This project used AI assistance during the Week 14 learning exercises and Week 15 capstone work.

## 1. What AI helped with

- Explaining class, object, init, methods, composition, and basic inheritance.
- Suggesting a simple Bot(strategy) design based on the Week 14 course notes.
- Drafting the balanced, defensive, and aggressive course-local strategies.
- Adding test cases for strategy injection and behavior on normal or invalid state.
- Drafting README sections for setup, usage, tests, design decisions, and limitations.

## 2. What the student must understand and verify

Before submission, I need to read the changed Python files and be able to explain:

- why Bot receives a strategy instead of hardcoding one policy;
- how Bot.choose_action() delegates to self.strategy(state);
- why the public choose_action(state) function remains for arena compatibility;
- how tests check normal, boundary, invalid-state, and strategy-swap behavior;
- why the local arena does not prove compatibility with the production VuaCóc runtime.

## 3. How the AI-assisted work is checked

Run these commands from the repository root:

```bash
python -m pytest projects/vuacoc-bot-journey/tests -q
python projects/vuacoc-bot-journey/local_arena/tournament_cli.py
python weeks/week-14-oop-essentials/checks/check_week.py
python weeks/week-15-capstone-project/checks/check_capstone_readiness.py projects/vuacoc-bot-journey
```

Test output and my own code review, not AI-generated claims, are the evidence of correctness.

## 4. Known limitations

- The strategies are simple teaching policies, not optimized gameplay.
- The local arena is a course exercise and is not the verified production runtime.
- I should update this disclosure if I make further substantial changes before submission.
