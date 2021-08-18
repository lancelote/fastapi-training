from typing import Optional

import fastapi
from fastapi import Depends

from models.location import Location
from models.report import Report
from models.report import ReportSubmittal
from models.validation_error import ValidationError
from services import openweather
from services import reports

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


@router.get("/api/reports", name="all_reports")
async def reports_get() -> list[Report]:
    return await reports.get_reports()


@router.post("/api/reports", name="add_report")
async def reports_post(report_submittal: ReportSubmittal) -> Report:
    description = report_submittal.description
    location = report_submittal.location
    return await reports.add_report(description, location)
