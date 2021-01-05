import fastapi
import uvicorn
from api import weather
from starlette.staticfiles import StaticFiles
from views import home

api = fastapi.FastAPI()
api.mount("/static", StaticFiles(directory="static"), name="static")
api.include_router(weather.router)
api.include_router(home.router)

if __name__ == "__main__":
    uvicorn.run(api, host="127.0.0.1", port=8000)
