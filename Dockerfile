FROM python:3.11-slim as base

WORKDIR /app

FROM base as builder

ENV POETRY_VERSION=1.6.1

RUN pip install "poetry==${POETRY_VERSION}"
RUN python -m venv /venv

COPY poetry.lock pyproject.toml ./
RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

COPY . ./
RUN poetry build && /venv/bin/pip install dist/*.whl

# Multi-stage example
# FROM base as final
# COPY --from=builder /venv /venv
# COPY docker-entrypoint.sh app.py ./
CMD ["./docker-entrypoint.sh"]