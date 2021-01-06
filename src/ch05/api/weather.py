from typing import Optional

import fastapi
from fastapi import Depends
from models.location import Location

router = fastapi.APIRouter()


@router.get("/api/weather/{city}")
def weather(location: Location = Depends(), units: Optional[str] = "metric"):
    return f"{location.city}, {location.state}, {location.country} in {units}"
