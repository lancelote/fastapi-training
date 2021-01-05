import fastapi
import uvicorn
from api import weather
from starlette.staticfiles import StaticFiles
from views import home

api = fastapi.FastAPI()


def configure_routing():
    api.include_router(weather.router)
    api.include_router(home.router)


def configure_static():
    api.mount("/static", StaticFiles(directory="static"), name="static")


def configure():
    configure_routing()
    configure_static()


if __name__ == "__main__":
    configure()
    uvicorn.run(api, host="127.0.0.1", port=8000)
else:
    configure()
