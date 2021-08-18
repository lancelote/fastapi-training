import datetime
import uuid

from models.location import Location
from models.report import Report

__reports: list[Report] = []


async def get_reports() -> list[Report]:
    # Would be an async call in the real application
    return __reports.copy()


async def add_report(description: str, location: Location) -> Report:
    now = datetime.datetime.now()
    report = Report(
        id=str(uuid.uuid4()),
        description=description,
        location=location,
        created_date=now,
    )

    # Simulate saving to a DB
    # Would be an async call in the real application
    __reports.append(report)

    __reports.sort(key=lambda x: x.created_date, reverse=True)

    return report
