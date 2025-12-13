# Dictionary MCP Server

## Overview
An MCP (Model Context Protocol) server for IELTS students/learners that provides easy access to word definitions through the Merriam-Webster Collegiate Dictionary API.

## Project Structure
- `dictionary.py` - Main MCP server with the `getDefinition` tool
- `main.py` - Entry point (unused, dictionary.py is the main file)
- `pyproject.toml` - Python project configuration with dependencies

## Dependencies
- `httpx` - HTTP client for API requests
- `mcp[cli]` - Model Context Protocol server library
- `python-dotenv` - Environment variable management

## Environment Variables
- `MERRIAM_API` - **Required** - Merriam-Webster API key (get one from https://dictionaryapi.com/)

## Running the Server
The MCP server runs with stdio transport:
```bash
python dictionary.py
```

## MCP Tools Available
- `getDefinition(word: str)` - Returns the definition of a word from Merriam-Webster dictionary
