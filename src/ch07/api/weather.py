from typing import Optional

import fastapi
from fastapi import Depends

from models.location import Location
from models.validation_error import ValidationError
from services import openweather

router = fastapi.APIRouter()


@router.get("/api/weather/{city}")
async def weather(loc: Location = Depends(), units: Optional[str] = "metric"):
    try:
        return await openweather.get_report(
            loc.city, loc.state, loc.country, units
        )
    except ValidationError as validation_error:
        return fastapi.Response(
            content=validation_error.error_message,
            status_code=validation_error.status_code,
        )
    except Exception as error:
        print(f"Server crashed while processing request: {error}")
        return fastapi.Response(
            content="Error processing request.", status_code=500
        )
