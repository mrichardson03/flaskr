# Agents

## Development Commands
- **Test**: `pytest`
- **Lint**: `ruff check .`
- **Lint (fix)**: `ruff check . --fix`
- **Coverage**: `pytest --cov=flaskr`

## Environment & Config
- **Database**: Uses SQLAlchemy. Configure via `DATABASE_URI` env var.
- **Python Version**: `3.13+`
- **Dependencies Management**: `uv`

## Workflow
- **Semantic Release**: Uses `python-semantic-release` for versioning and changelog generation.
- **Deployment**: Helm charts available in `deployment/charts/flaskr/` (referenced in `pyproject.toml`).
