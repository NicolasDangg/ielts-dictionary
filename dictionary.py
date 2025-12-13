import os

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

load_dotenv()
api_key = os.getenv("MERRIAM_API")
PORT = int(os.environ.get("PORT", 8000))

mcp = FastMCP("dictionary", host="0.0.0.0", port=PORT)


async def make_merriam_request(word: str) -> list | None:
    """Make a request to the Merriam-Webster Dictionary API"""
    url = f"https://dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"
    headers = {"Accept": "application/json"}

    async with httpx.AsyncClient(follow_redirects=True) as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None


def format_definition(data: list | None) -> str:
    """Format dictionary data into an output string"""
    if data is None or not isinstance(data, list) or len(data) == 0:
        return "No definition found"

    entry = data[0]  # get the first entry from API response
    word = entry.get("hwi", {}).get(
        "hw", "Unknown"
    )  # hwi: headword information, hw: headword, unknown if missing
    part_of_speech = entry.get("fl", "Unknown")
    definitions = entry.get("shortdef", [])

    result = f"Word: {word}\n"
    result += f"Part of speech: {part_of_speech}\n"
    result += "Definitions:\n"
    for i, definition in enumerate(
            definitions,
            1):  # counting variables without incrementing anything
        result += f" {i}. {definition}\n"  # output definitions one by one

    return result


@mcp.tool()
async def getDefinition(word: str) -> str:
    """Get definition from Merriam-Webster API"""
    data = await make_merriam_request(word)
    if data is None:
        return "Error: Could not fetch definition"
    return format_definition(data)


def main():
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()
