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
- `PORT` - Optional - Server port (defaults to 8000)

## Running the Server
The MCP server runs with streamable-http transport on port 8000:
```bash
python dictionary.py
```

The server will be available at `http://0.0.0.0:8000/mcp`

## MCP Tools Available
- `getDefinition(word: str)` - Returns the definition of a word from Merriam-Webster dictionary

## Deploying on Render

1. Create a new Web Service on Render
2. Connect your GitHub repository
3. Set the following:
   - **Build Command**: `pip install -r requirements.txt` (or use `uv sync`)
   - **Start Command**: `python dictionary.py`
4. Add environment variables:
   - `MERRIAM_API` - Your Merriam-Webster API key
   - `PORT` - Render sets this automatically
5. Deploy

Your MCP server will be available at: `https://your-app.onrender.com/mcp`

### Connecting MCP Clients
Configure your MCP client to connect to the streamable-http endpoint:
```json
{
  "mcpServers": {
    "dictionary": {
      "transport": {
        "type": "streamable-http",
        "url": "https://your-app.onrender.com/mcp"
      }
    }
  }
}
```
