from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routers import check, about
from starlette.staticfiles import StaticFiles
from starlette import status

# Class Instance
app = FastAPI()

# Static Files
app.mount('/static', StaticFiles(directory="server/static"), name="static")

# Routers
app.include_router(check.router)
app.include_router(about.router)

# Handlers
@app.get("/")
async def default_route():
    return RedirectResponse(url='/check', status_code=status.HTTP_302_FOUND)

@app.exception_handler(404)
async def not_found(request, exc):
    return RedirectResponse(url='/check', status_code=status.HTTP_302_FOUND)