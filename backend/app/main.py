from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os

app = FastAPI(title="SmartDevice Embedded Systems Lab")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

frontend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "frontend"))
templates_dir = os.path.join(frontend_dir, "templates")
templates = Jinja2Templates(directory=templates_dir)

try:
    from .api import devices, tests
    from .websocket import telemetry
    app.include_router(devices.router, prefix="/api/devices", tags=["devices"])
    app.include_router(tests.router, prefix="/api/tests", tags=["tests"])
    app.include_router(telemetry.router)
except Exception as e:
    print("Router include error:", e)

@app.get("/", response_class=HTMLResponse)
async def page_dashboard(request: Request):
    return templates.TemplateResponse(request=request, name="dashboard.html")

@app.get("/devices", response_class=HTMLResponse)
async def page_devices(request: Request):
    return templates.TemplateResponse(request=request, name="devices.html")

@app.get("/hardware", response_class=HTMLResponse)
async def page_hardware(request: Request):
    return templates.TemplateResponse(request=request, name="hardware.html")

@app.get("/tests", response_class=HTMLResponse)
async def page_tests(request: Request):
    return templates.TemplateResponse(request=request, name="tests.html")

@app.get("/alerts", response_class=HTMLResponse)
async def page_alerts(request: Request):
    return templates.TemplateResponse(request=request, name="alerts.html")

@app.get("/settings", response_class=HTMLResponse)
async def page_settings(request: Request):
    return templates.TemplateResponse(request=request, name="settings.html")

@app.get("/api/health")
def health():
    return {"status": "ok"}
