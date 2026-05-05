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

### 1. Tutorial Agent

A minimal starter agent with one mock time tool. See `src/tutorials/t01_tutorial_agent/README.md`.

### 2. Basic ADK Agent

A single agent with one Python function tool (dice rolling). See `src/tutorials/t02_basic_agent/README.md`.

### 3. Sequential Workflow Agent

A deterministic pipeline using `SequentialAgent`: two sub-agents run in a fixed order defined in code (researcher then summarizer), not decided by an LLM. See `src/tutorials/t03_sequential_agent/README.md`.

### 4. Multi-Agent (Local)

A supervisor agent orchestrating two local sub-agents (dice roller + stats calculator) using `AgentTool`. See `src/tutorials/t04_multi_agent/README.md`.

### 5. ADK Agent with MCP Tool

A step-by-step MCP tutorial: run a separate notes MCP server and connect to it from both a standalone client and an ADK agent. See `src/tutorials/t05_mcp_agent/README.md`.

### 6. Remote A2A Agents

Three remote agents communicating via the A2A protocol, each with its own agent card and HTTP server. See `src/tutorials/t06_remote_a2a/README.md`.

### 7. Agent Evaluations with DeepEval

Evaluate the multi-agent supervisor with a golden dataset and DeepEval metrics. See `src/tutorials/t07_evaluations/README.md`.

Install eval dependencies:

```bash
uv sync --extra adk --extra eval
uv run pytest src/tutorials/t07_evaluations/ -v
```

### 8. Deploy ADK Agent to GCP

Deploy a self-contained dice agent to Cloud Run and Vertex AI Agent Engine using `adk deploy`. See `src/tutorials/t08_deploy_gcp/README.md`.

## Notebooks

Install notebook dependencies and start Jupyter:

```bash
uv sync --extra notebooks
uv run jupyter notebook notebooks/
```

- `notebooks/deploy_gcp_clients.ipynb`: call the deployed GCP agent from Cloud Run and Agent Engine.
