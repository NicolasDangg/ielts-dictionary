import os

import httpx
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP
from mcp.types import Result
import requests

load_dotenv()
api_key = os.getenv("MERRIAM_API")
PORT = int(os.environ.get("PORT", 8000))

mcp = FastMCP("dictionary", host="0.0.0.0", port=PORT)

currency_u = "https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/usd.json"


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

def list_of_deals():
    deals_url = "https://www.cheapshark.com/api/1.0/deals?storeID=1,25&upperPrice=10"
    store_url = "https://www.cheapshark.com/api/1.0/stores"

    currency_r = requests.request("GET", currency_u)
    currency_o = currency_r.json()
    ##print(json.dumps(currency_o, indent=2))
    ##print([key for key in currency_o.keys()])
    usd_dict = currency_o["usd"]
    vnd_rate = usd_dict["vnd"]
    ##c = currency_output[0]
    ##vnd_rate = c.get("vnd")

    deals_r = requests.request("GET", deals_url)
    deals_o = deals_r.json()

    store_response = requests.request("GET", store_url)
    store_output = store_response.json()
    store_map = {storeID["storeID"]: storeID["storeName"] for storeID in store_output}

    ##print(deals_output)

    for i in range(0, len(deals_o)):
        entry = deals_o[i]
        gameName = entry.get("title", "Unknown")
        gameId = entry.get("gameID", "Unknown")
        salePriceGet = entry.get("salePrice")
        salePrice = float(salePriceGet) * float(vnd_rate)
        normalPriceGet = entry.get("normalPrice")
        normalPrice = float(normalPriceGet) * float(vnd_rate)
        sale = entry.get("isOnSale")
        steamRatingText = entry.get("steamRatingText")
        steamRatingPercent = entry.get("steamRatingPercent")
        storeID = entry.get("storeID")
        storeName = store_map.get(storeID)

        result = f"Game name: {gameName}\n"
        result += f"Game ID: {gameId}\n"
        result += f"Store: {storeName}\n"
        result += f"Sale Price: {'Free' if float(salePrice) == 0.0 else f'{round(float(salePrice) / 1000)}.000 VND'}\n"
        result += f"Normal Price: {'Free' if float(normalPrice) == 0.0 else (f'{float(normalPrice) / 1000000:.3f} M VND' if float(normalPrice) >= 1000000 else f'{round(float(normalPrice) / 1000)}.000 VND')}\n"
        result += f"On Sale: {'Yes' if sale == '1' else 'No'}\n"
        result += f"Steam Rating: {steamRatingText} ({steamRatingPercent}%)\n"
        result += "-----------------------------\n"
        return result

def freeGames(number: int):
    games_u = "https://www.freetogame.com/api/games"
    games_r = requests.request("GET", games_u)
    games_o = games_r.json()


    for i in range(0, number):
        entry = games_o[i]
        ##print(entry)
        gameName = entry.get("title")
        genre = entry.get("genre")
        platform = entry.get("platform")
        publisher = entry.get("publisher")
        release = entry.get("release_date")

        result = f"Game name: {gameName}\n"
        result += f"Genre: {genre}\n"
        result += f"Platform(s): {platform}\n"
        result += f"Publisher: {publisher}\n"
        result += f"Release date: {release}\n"
        result += "------------------\n"

        return result

@mcp.tool()
async def getDefinition(word: str) -> str:
    """Get definition from Merriam-Webster API"""
    data = await make_merriam_request(word)
    if data is None:
        return "Error: Could not fetch definition"
    return format_definition(data)

@mcp.tool()
async def getDeals():
    """List game deals below $10 in VND"""
    list_of_deals()

@mcp.tool()
async def getFreeGames(number):
    """Free games sorted by name and platform"""
    freeGames(number)

def main():
    mcp.run(transport="streamable-http")


if __name__ == "__main__":
    main()
