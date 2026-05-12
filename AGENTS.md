# OpenCode Guide: Development & Workflow Best Practices

## Environment

- Python 3.13+ required. Dependencies managed via `uv`.
- Install: `uv sync --locked --all-extras --dev`
- `DATABASE_URI` env var sets the DB connection string (SQLAlchemy URI). Defaults to SQLite at `instance/flaskr.db`.
- For MySQL, use the `pymysql` driver: `mysql+pymysql://...`

## Testing

Tests use in-memory SQLite — no external database needed.

```
uv run pytest
uv run pytest --cov=flaskr   # coverage (uses 'coverage' package, not pytest-cov)
uv run pytest tests/test_auth.py::test_login  # single test
```

CI runs `mkdir instance && uv run flask init-db` before pytest when using a real DB. For local test runs with in-memory SQLite this is not required — conftest handles DB setup via fixtures.

## Linting & Formatting

Pre-commit enforces both lint and format via `ruff`:

```
ruff check .          # lint
ruff check . --fix    # auto-fix lint
ruff format .         # format (separate from lint)
```

`.flake8` exists but is legacy — `ruff` is the enforced tool.

## Running Locally

```
FLASK_APP=flaskr uv run flask run
```

The app auto-creates DB tables on startup if the `user` table is missing. Use `flask init-db` to wipe and reinitialize the database.

## Source Layout

- App package: `src/flaskr/` (src layout — `PYTHONPATH` is managed by `uv`)
- Entrypoint/factory: `src/flaskr/__init__.py` → `create_app()`
- Blueprints: `auth.py`, `blog.py`
- Models: `models.py`
- Instance dir (`instance/`) is created automatically by the app but must exist before `flask init-db` runs.

## Commit Messages

Uses Conventional Commits. `python-semantic-release` drives versioning:
- `feat:` → minor bump
- `fix:`, `perf:` → patch bump
- `chore:`, `ci:`, `docs:`, `refactor:`, `style:`, `test:` → excluded from changelog

## Release / Build

Releases are automated via `python-semantic-release` on `main`. The build command updates `uv.lock`, bumps versions in `pyproject.toml` and `deployment/charts/flaskr/Chart.yaml`, then runs `uv build`. Do not manually edit version fields.

## Deployment

Helm charts: `deployment/charts/flaskr/`. Chart version is kept in sync with app version by semantic-release.
