from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import detector, about
from starlette.staticfiles import StaticFiles

# Class Instance
app = FastAPI()

# Static Files
app.mount('/static', StaticFiles(directory="static"), name="static")

# Routers
app.include_router(detector.router)
app.include_router(about.router)

@app.get("/")
async def default_route():
    return RedirectResponse(url='/detector')