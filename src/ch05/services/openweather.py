import httpx

api_key: str | None = None


async def get_report(
    city: str, state: str | None, country: str, units: str
) -> dict:
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    if state:
        query = f"{city},{state},{country}"
    else:
        query = f"{city},{country}"
    url = f"{base_url}?q={query}&appid={api_key}&units={units}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()

    data = response.json()
    forecast = data["main"]
    return forecast
