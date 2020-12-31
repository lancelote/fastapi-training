import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get("/api/calculate")
def calculate(x: int, y: int, z: int = 10):
    value = (x + y) * z
    return {"value": value}


if __name__ == "__main__":
    uvicorn.run(api, host="127.0.0.1", port=8000)
