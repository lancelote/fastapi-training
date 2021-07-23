from typing import Optional

import fastapi
from fastapi import Depends

from models.location import Location
from services import openweather

router = fastapi.APIRouter()


@router.get("/api/weather/{city}")
async def weather(loc: Location = Depends(), units: Optional[str] = "metric"):
    report = await openweather.get_report(
        loc.city, loc.state, loc.country, units
    )
    return report
