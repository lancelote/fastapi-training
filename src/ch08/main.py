import json
from pathlib import Path

import fastapi
import uvicorn
from starlette.staticfiles import StaticFiles

from api import weather
from services import openweather
from views import home

api = fastapi.FastAPI()


def configure_routing():
    api.include_router(weather.router)
    api.include_router(home.router)


def configure_static():
    api.mount("/static", StaticFiles(directory="static"), name="static")


def configure_api_keys():
    file = Path("settings.json").absolute()
    if not file.exists():
        raise Exception(
            "settings.json not found,"
            "your cannot continue,"
            "please see settings_template.json"
        )

    with open(file) as settings_json:
        settings = json.load(settings_json)
        openweather.api_key = settings.get("api_key")


def configure():
    configure_routing()
    configure_static()
    configure_api_keys()


if __name__ == "__main__":
    configure()
    uvicorn.run(api, host="127.0.0.1", port=8000)
else:
    configure()
