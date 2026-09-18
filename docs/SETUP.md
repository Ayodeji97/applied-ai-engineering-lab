# Setup

## Requirements

- VS Code
- Python 3.12+
- Git
- `uv`

## Open the project

```bash
code applied-ai-engineering-labs
```

## Install the development environment

From the repository root:

```bash
uv sync
```

VS Code should select `.venv/bin/python`. If it does not:

1. Open the command palette.
2. Choose **Python: Select Interpreter**.
3. Select the interpreter inside `.venv`.

## Verify the tools

```bash
uv run python --version
uv run ruff check .
uv run pyright
uv run pytest
```

The first `pytest` run should fail because the first independent implementation is intentionally unfinished.

## Publish to GitHub from VS Code

After signing in to GitHub inside VS Code:

1. Open **Source Control**.
2. Review the files; do not commit `.venv` or secrets.
3. Set your Git author name/email if VS Code requests it.
4. Commit with: `chore: scaffold applied AI engineering labs`.
5. Choose **Publish Branch** or **Publish to GitHub**.
6. Start as a private repository unless you intentionally want unfinished exercises public.

