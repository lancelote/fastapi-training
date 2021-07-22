api_key: str | None = None


def get_report(city: str, state: str | None, country: str, units: str) -> dict:
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    query = f"{city},{country}"
    url = f"{base_url}?q={query}&appid={api_key}&units={units}"
    print(url)
