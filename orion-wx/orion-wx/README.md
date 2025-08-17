# orion-wx

Open U.S. weather AI: ingest NOAA/NASA, blend NWP+ML+nowcasting (optional solar/lunar), serve API & map UI

## Quickstart

```bash
# 1) Create environment (uv or pip)
pip install -e ".[dev]"

# 2) Run API
uvicorn src.api.main:app --reload --port 8000

# 3) Open API docs
# http://localhost:8000/docs

# 4) Run tests & linters
pytest -q
ruff check . && ruff format --check .
```

## What’s here

- **API**: FastAPI service exposing `/health`, `/forecast` (mock) and ready hooks for probabilistic outputs.
- **Ingestion**: placeholders for NEXRAD/GOES, stations, and NWP feeds.
- **Nowcasting**: `pySTEPS`-ready module skeleton.
- **Post-processing**: calibration stubs (EMOS/isotonic).
- **Verification**: metrics scaffolding (CRPS/Brier hooks).
- **Infra**: Dockerfile, Makefile, GitHub Actions CI.

## License

Apache-2.0 © Orion WX Contributors
