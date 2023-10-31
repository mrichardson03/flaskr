FROM python:3.11-slim as base

FROM base as develop

WORKDIR /app

ARG POETRY_VERSION=1.6.1

ENV FLASK_APP=flaskr

RUN pip install "poetry==${POETRY_VERSION}"
RUN python -m venv /venv

COPY poetry.lock pyproject.toml ./
# RUN poetry install

# EXPOSE 5000
# ENTRYPOINT ["/venv/bin/python3", "-m", "flask", "run", "--host=0.0.0.0"]

RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

COPY . ./
RUN poetry build && /venv/bin/pip install dist/*.whl

# Multi-stage example
FROM base as final
COPY --from=builder /venv /venv
COPY docker-entrypoint.sh app.py ./
CMD ["./docker-entrypoint.sh"]
