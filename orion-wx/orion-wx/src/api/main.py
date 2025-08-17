from fastapi import FastAPI
from pydantic import BaseModel
from .settings import settings

app = FastAPI(title="Orion WX API", version="0.1.0")

class ForecastRequest(BaseModel):
    lat: float
    lon: float
    lead_hours: int = 24
    variable: str = "precip"

@app.get("/health")
def health():
    return {"status": "ok", "env": settings.APP_ENV}

@app.post("/forecast")
def forecast(req: ForecastRequest):
    # Placeholder probabilistic response (replace with calibrated outputs)
    # Return quantiles and event probabilities
    return {
        "meta": {
            "lat": req.lat,
            "lon": req.lon,
            "lead_hours": req.lead_hours,
            "variable": req.variable,
            "provenance": ["NBM", "HRRR", "HREF", "GEFS"],
        },
        "quantiles": {"p10": 0.2, "p50": 0.8, "p90": 1.6},
        "event_probs": {">=1in_24h": 0.35},
    }
