# AGENTTEST

A small, deterministic fixture project used to prove out PROTO-CODEX-INFOTEL's
`agent_workflow` campaign controller: multiple independent tasks running
concurrently against isolated worktrees/branches, with all git integration
(commits, pushes, PRs, merges) owned exclusively by the controller.

This repository has no other purpose — it is intentionally trivial so that
correctness of the *orchestration* (isolation, conflict handling, gating,
crash-resume) can be judged independently of the *code being generated*.

## Layout

- `calc/add_sub.py` — `add(a, b)`, `sub(a, b)`
- `calc/mul_div.py` — `mul(a, b)`, `div(a, b)` (raises `ZeroDivisionError`)
- `calc/cli.py` — trivial CLI dispatch over the above
- `tests/` — pytest suite, deterministic, no network/time/randomness
- `.github/workflows/ci.yml` — runs the test suite on push/PR

## Running tests

```
pip install pytest
pytest -v
```
