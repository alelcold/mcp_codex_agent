# mcp_codex_agent

A CLI tool for interacting with MCP Chat Workflow Engine and OpenAI Codex to automate software development using natural language.

## 🚀 Features

- Run natural language prompts to trigger Codex-generated code
- Dry-run mode with git diff preview
- Approval mode to auto-apply changes
- Color-coded terminal output for better UX
- `.env` support for environment config

## 📦 Structure

```
mcp_codex_agent/
├── __init__.py
├── cli.py             # CLI entrypoint with typer
├── codex_client.py    # Handles HTTP calls to MCP backend
├── diff_utils.py      # Git diff utilities
├── config.py          # Loads .env and config vars
├── main.py            # Entry point if imported as a module
├── templates/         # Optional, for future plugin support
.env                   # Stores MCP_CLI_API url
pyproject.toml         # Defines dependencies and CLI command
README.md              # You are here
```

## 🛠 Installation

```bash
git clone https://github.com/yourname/mcp-codex-agent.git
cd mcp-codex-agent
pip install -e .
```

Make sure your `.env` is set correctly:
```
MCP_CLI_API=http://localhost:8000
```

## 🔧 Usage

```bash
mcp-codex "generate FastAPI endpoint /hello" --path ./myproject
mcp-codex "add logging" --dry-run --path ./myproject
mcp-codex "add JWT auth" --approve --path ./myproject
```

## 🔮 Roadmap

- Plugin registry for multi-language Codex agents
- Chat history & persistent workflow context
- GitHub Actions integration for CI/CD agent workflows
- Enhanced diff and rollback tools

## 📄 License
MIT
