# OpenCode Guide: Development & Workflow Best Practices

**Development Commands & Conventions**

*   **Testing**: Tests are run using `pytest`. Coverage reports should be generated with `pytest --cov=flaskr`.
*   **Linting**: Use `ruff` for mandatory code quality checks:
    *   Check: `ruff check .`
    *   Fix: `ruff check . --fix`
*   **Environment**:
    *   Database: Uses SQLAlchemy. Requires `DATABASE_URI` environment variable.
    *   Dependencies: Managed via `uv`.
    *   Python Version: Requires 3.13+.

**Workflow & Deployment**

*   **Semantic Release**: Versioning must use `python-semantic-release`.
*   **Deployment**: Helm charts are available in `deployment/charts/flaskr/` (referenced in `pyproject.toml`).
