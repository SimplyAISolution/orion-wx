FROM python:3.11-slim

WORKDIR /app
COPY pyproject.toml README.md ./
RUN pip install --upgrade pip && pip install uv && uv pip install --system -e .[dev]

COPY src ./src
EXPOSE 8000
CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
