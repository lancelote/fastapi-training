from typing import Optional

import httpx
from httpx import Response

from infrastructure import cache
from models.validation_error import ValidationError

api_key: Optional[str] = None


async def get_report(
    city: str, state: Optional[str], country: str, units: str
) -> dict:
    city, state, country, units = validate_units(city, state, country, units)

    if forecast := cache.get_weather(city, state, country, units):
        return forecast

    base_url = "https://api.openweathermap.org/data/2.5/weather"
    if state:
        query = f"{city},{state},{country}"
    else:
        query = f"{city},{country}"
    url = f"{base_url}?q={query}&appid={api_key}&units={units}"

    async with httpx.AsyncClient() as client:
        response: Response = await client.get(url)

        if response.status_code != 200:
            raise ValidationError(response.text, response.status_code)

    data = response.json()
    forecast = data["main"]

    cache.set_weather(city, state, country, units, forecast)
    return forecast


def validate_units(
    city: str, state: Optional[str], country: str, units: str
) -> tuple[str, Optional[str], str, str]:
    city = city.lower().strip()
    if not country:
        country = "us"
    else:
        country = country.lower().strip()

    if len(country) != 2:
        error_message = (
            f"Invalid country: {country}."
            f" It should be two letter abbreviation such as US."
        )
        raise ValidationError(error_message, status_code=404)

    if state:
        state = state.lower().strip()

    if state and len(state) != 2:
        error_message = (
            f"Invalid state: {state}."
            f" It should be two letter abbreviation such as CA."
        )
        raise ValidationError(error_message, status_code=404)

    if units:
        units = units.lower().strip()

    valid_units = {"standard", "metric", "imperial"}
    if units not in valid_units:
        error_message = (
            f"Invalid units: {units}." f" Must be one of {valid_units}."
        )
        raise ValidationError(error_message, status_code=404)

    return city, state, country, units
