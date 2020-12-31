from typing import Optional

import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get("/api/calculate")
def calculate(x: int, y: int, z: Optional[int] = None):
    value = x + y

    if z is not None:
        value /= z

    return {"x": x, "y": y, "z": z, "value": value}


if __name__ == "__main__":
    uvicorn.run(api, host="127.0.0.1", port=8000)
