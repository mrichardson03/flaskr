FROM python:3.11-slim as base

FROM base as develop

WORKDIR /app

# renovate: datasource=github-releases depName=poetry packageName=python-poetry/poetry
ARG POETRY_VERSION=1.8.3

ENV FLASK_APP=flaskr

RUN pip install "poetry==${POETRY_VERSION}"
RUN python -m venv /venv

COPY poetry.lock pyproject.toml ./
RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

COPY . ./
RUN poetry build && /venv/bin/pip install dist/*.whl

# Multi-stage example
FROM base as final

# Fix CVE-2024-45490, CVE-2024-45491, CVE-2024-45492 in base image.
RUN apt-get update && apt-get install -y --no-install-recommends libexpat1=2.5.0-1+deb12u1

COPY --from=develop /venv /venv
COPY docker-entrypoint.sh ./
CMD ["./docker-entrypoint.sh"]
