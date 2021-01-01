from typing import Optional

import fastapi
import uvicorn

api = fastapi.FastAPI()


@api.get("/")
def index():
    body = """
        <html>
        <body style='padding: 10px;'>
        <h1>Welcome to the API</h1>
        <div>
        Try it: <a href='/api/calculate?x=7&y=11'>/api/calculate?x=7&y=11</a>
        </div>
        </body>
        </html>
    """
    return fastapi.responses.HTMLResponse(content=body)


@api.get("/api/calculate")
def calculate(x: float, y: float, z: Optional[float] = None):
    if z == 0:
        return fastapi.responses.JSONResponse(
            content={"error": "z cannot be zero"},
            status_code=400,
        )

    value = x + y

    if z is not None:
        value /= z

    return {"x": x, "y": y, "z": z, "value": value}


if __name__ == "__main__":
    uvicorn.run(api, host="127.0.0.1", port=8000)
