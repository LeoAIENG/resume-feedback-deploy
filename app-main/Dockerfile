# IMAGE
ARG PYTHON_V=3.11
FROM ghcr.io/astral-sh/uv:python${PYTHON_V}-bookworm-slim

WORKDIR /app

# UV CONFIG
ENV PATH="/app/.venv/bin:$PATH"
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --frozen --no-install-project --no-dev

# COPY
ADD . /app

# INSTALL
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-dev
RUN python${PYTHON_V} -c "import nltk; nltk.download('punkt'); nltk.download('punkt_tab')"

ENTRYPOINT []

# APP
ENV APP_TIMEOUT=1200
ENV NUM_WORKERS=4
ENV SERVER_PORT=8086
ENV LOG_LEVEL=debug

CMD gunicorn app:app \
	--workers $NUM_WORKERS \
	--worker-class uvicorn.workers.UvicornWorker \
	--bind 0.0.0.0:$SERVER_PORT \
	--timeout $APP_TIMEOUT \
	--log-level $LOG_LEVEL