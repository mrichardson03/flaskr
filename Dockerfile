FROM python:3.11-slim AS base

FROM base AS develop

WORKDIR /app

# renovate: datasource=github-releases depName=poetry packageName=python-poetry/poetry
ARG POETRY_VERSION=1.8.5

ENV FLASK_APP=flaskr

RUN apt-get update && apt-get install -y --no-install-recommends \
  gcc build-essential libssl-dev libffi-dev python3-dev

RUN pip install "poetry==${POETRY_VERSION}"
RUN python -m venv /venv

COPY poetry.lock pyproject.toml ./
RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

COPY . ./
RUN poetry build && /venv/bin/pip install dist/*.whl

# Multi-stage example
FROM base AS final

# Fix CVE-2024-45490, CVE-2024-45491, CVE-2024-45492 in base image.
RUN apt-get update && apt-get install -y --no-install-recommends libexpat1=2.5.0-1+deb12u1

COPY --from=develop /venv /venv
COPY docker-entrypoint.sh ./
CMD ["./docker-entrypoint.sh"]
