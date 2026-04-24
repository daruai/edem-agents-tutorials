# agents-tutorials

Agents tutorials and examples.

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```bash
# Create venv and install project + dev dependencies
uv sync

# Run a script
uv run python -c "from agents_tutorials import __version__; print(__version__)"
```

### Install tutorial dependencies

```bash
uv sync --extra adk
```

### Model provider options

All tutorials read the same env vars from `.env.example`.

#### Option A: Gemini (default)

```bash
export GOOGLE_API_KEY="your-gemini-api-key"
```

#### Option B: Groq

```bash
export MODEL_PROVIDER=groq
export GROQ_API_KEY="your-groq-api-key"
```

#### Option C: Vertex AI

One-time auth on your machine:

```bash
gcloud auth application-default login
```

Then configure Vertex:

```bash
export MODEL_PROVIDER=vertex
export GOOGLE_CLOUD_PROJECT="your-gcp-project-id"
export GOOGLE_CLOUD_LOCATION="global"
# optional
export VERTEX_MODEL="gemini-2.5-flash-lite"
```

## Project structure

```text
├── notebooks/          # Jupyter notebooks
├── src/
│   ├── agents_tutorials/
│   └── tutorials/      # Step-by-step tutorials (ADK, MCP, A2A, evals)
├── pyproject.toml
└── README.md
```

## Tutorials

### 1. Basic ADK Agent

A single agent with one Python function tool (dice rolling). See `src/tutorials/basic_agent/README.md`.

### 2. Multi-Agent (Local)

A supervisor agent orchestrating two local sub-agents (dice roller + stats calculator) using `AgentTool`. See `src/tutorials/multi_agent/README.md`.

### 3. ADK Agent with MCP Tool

A step-by-step MCP tutorial: run a separate notes MCP server and connect to it from both a standalone client and an ADK agent. See `src/tutorials/mcp_agent/README.md`.

### 4. Remote A2A Agents

Three remote agents communicating via the A2A protocol, each with its own agent card and HTTP server. See `src/tutorials/remote_a2a/README.md`.

### 5. Sequential Workflow Agent

A deterministic pipeline using `SequentialAgent`: two sub-agents run in a fixed order defined in code (researcher then summarizer), not decided by an LLM. See `src/tutorials/sequential_agent/README.md`.

### 6. Agent Evaluations with DeepEval

Evaluate the multi-agent supervisor with a golden dataset and DeepEval metrics. See `src/tutorials/evaluations/README.md`.

Install eval dependencies:

```bash
uv sync --extra adk --extra eval
uv run pytest src/tutorials/evaluations/ -v
```

## Notebooks

Install notebook dependencies and start Jupyter:

```bash
uv sync --extra notebooks
uv run jupyter notebook notebooks/
```
