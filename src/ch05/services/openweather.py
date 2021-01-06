from typing import Dict
from typing import Optional


def get_report(
    city: str, state: Optional[str], country: str, units: str
) -> Dict:
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    query = f"{city},{country}"
    key = 123
    url = f"{base_url}?q={query}&appid={key}&units={units}"
    print(url)
