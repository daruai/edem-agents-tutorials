"""ADK agent with MCP tool: uses the filesystem MCP server to explore files."""

import os

from google.adk import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

from model_config import get_model

SANDBOX_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sandbox")

root_agent = Agent(
    model=get_model(),
    name="filesystem_agent",
    description="Explores and reads files in a sandbox directory using MCP filesystem tools.",
    instruction=(
        "You are a file-system assistant. You help the user explore and read files "
        "in the sandbox directory.\n"
        "Use the available tools to list directories and read file contents.\n"
        "When listing files, present the results clearly.\n"
        "When reading a file, show its full content."
    ),
    tools=[
        McpToolset(
            connection_params=StdioConnectionParams(
                timeout=30,
                server_params=StdioServerParameters(
                    command="npx",
                    args=[
                        "-y",
                        "@modelcontextprotocol/server-filesystem",
                        SANDBOX_PATH,
                    ],
                ),
            ),
            tool_filter=["list_directory", "read_file"],
        ),
    ],
)
