# Basic ADK Agent

The simplest ADK agent: a single agent with one Python function tool that rolls dice.

## Concepts

- `Agent` with `instruction`, `description`, and `tools`
- Python function as an agent tool
- Running agents with `adk web`

## Setup

```bash
uv sync --extra adk
```

### Option A: Gemini (default)

```bash
export GOOGLE_API_KEY="your-gemini-api-key"
```

### Option B: Groq

```bash
export MODEL_PROVIDER=groq
export GROQ_API_KEY="your-groq-api-key"
```

## Run

```bash
uv run adk web tutorials/basic_agent
```

Open http://localhost:8000, pick **roll_die**, and try:

- "Roll a 6-sided die 3 times"
- "Roll a 20-sided die"
- "Roll a die 10 times"
