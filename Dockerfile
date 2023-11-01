FROM python:3.12-slim as base

FROM base as develop

WORKDIR /app

ARG POETRY_VERSION=1.6.1

ENV FLASK_APP=flaskr

RUN pip install "poetry==${POETRY_VERSION}"
RUN python -m venv /venv

COPY poetry.lock pyproject.toml ./
RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

COPY . ./
RUN poetry build && /venv/bin/pip install dist/*.whl

# Multi-stage example
FROM base as final
COPY --from=develop /venv /venv
COPY docker-entrypoint.sh ./
CMD ["./docker-entrypoint.sh"]
