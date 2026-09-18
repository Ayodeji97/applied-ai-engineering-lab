# Applied AI Engineering Labs

Daniel Ogunleye's build-first path from senior Android engineering into applied AI engineering.

## How this repository works

Each lab introduces concepts only when a working feature needs them:

1. Build the smallest useful version.
2. Run tests and observe failures.
3. Learn the missing Python or AI concept.
4. Implement the feature yourself.
5. Explain the important decisions.
6. Submit code, test output, and a short reflection for review.

The labs are practice. The polished portfolio projects will later become separate repositories:

- StitchPad Intelligent Import
- Focused AgricTech Knowledge Assistant

## Learning path

| Lab | Outcome | Status |
|---|---|---|
| `01-workshop-order-cli` | Python foundations through a useful Workshop order tool | Start here |
| `02-order-api` | FastAPI, Pydantic, async I/O and persistence | Locked |
| `03-structured-ai-extraction` | LLM structured output and evaluation | Locked |
| `04-semantic-search` | Embeddings and retrieval fundamentals | Locked |
| `05-rag-assistant` | Grounded answers, citations and RAG evaluation | Locked |
| `06-tool-calling-workflow` | Tools, state, approval and recovery | Locked |
| `07-mcp-server` | MCP tools, resources, authentication and permissions | Locked |
| `08-production-ai` | Docker, CI, tracing, security and deployment | Locked |
| `09-mobile-ai` | Android/KMP integration and on-device benchmarking | Locked |

"Locked" means that the folder is documented but should not be implemented before the preceding competency gate is passed.

## Start

Read, in order:

1. [`docs/SETUP.md`](docs/SETUP.md)
2. [`docs/LEARNING_CONTRACT.md`](docs/LEARNING_CONTRACT.md)
3. [`01-workshop-order-cli/README.md`](01-workshop-order-cli/README.md)

Then run:

```bash
uv sync
uv run pytest
```

The first tests are expected to fail. Your first task is to make the balance calculation pass without asking a coding agent for the final implementation.

