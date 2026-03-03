# ADK Agent with MCP Tool

An ADK agent that gets its tools from an external MCP server instead of Python functions. Uses the `@modelcontextprotocol/server-filesystem` MCP server to explore a sandbox directory.

## Concepts

- `McpToolset`: connects an ADK agent to any MCP server
- `StdioConnectionParams`: launches a local MCP server process via stdin/stdout
- MCP tool discovery: the agent automatically discovers tools from the MCP server

## Prerequisites

- **Node.js / npx**: the filesystem MCP server runs as a Node.js process. Install from https://nodejs.org/

Verify npx is available:

```bash
which npx
```

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
uv run adk web tutorials/mcp_agent
```

Open http://localhost:8000, pick **filesystem**, and try:

- "List all files in the sandbox"
- "Read the contents of sample.txt"
- "What is in the notes folder?"
- "Read the welcome file"
