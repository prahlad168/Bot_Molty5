# syntax=docker/dockerfile:1
FROM python:3.11-slim AS base

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ============================================================
# Test stage — lint + pytest
# ============================================================
FROM base AS test

COPY requirements-test.txt .
RUN pip install --no-cache-dir -r requirements-test.txt

COPY . .

RUN ruff check app/ bot/ tests/
RUN pytest tests/ -v --tb=short

# ============================================================
# Production stage — minimal runtime image
# ============================================================
FROM base AS production

COPY bot/ ./bot/
RUN mkdir -p /app/dev-agent /root/.molty-royale

EXPOSE 8080

CMD ["python", "-m", "bot.main"]
