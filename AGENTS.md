# OpenCode Guide: Development & Workflow Best Practices

**Development Commands & Conventions**

*   **Testing**: Tests are run using `pytest`. Coverage reports should be generated with `pytest --cov=flaskr`. Use `pytest-cov` for coverage tracking.
*   **Linting**: Use `ruff` for mandatory code quality checks:
    *   Check: `ruff check .`
    *   Fix: `ruff check . --fix`
*   **Environment**:
    *   Database: Uses SQLAlchemy. Requires `DATABASE_URI` environment variable.
    *   Dependencies: Managed via `uv`.
    *   Python Version: Requires 3.13+.

**Workflow & Deployment**

*   **Build Process**: Use `uv build` for creating distributions. Building also involves updating the `uv.lock` file as part of the semantic release workflow.
*   **Deployment**: Helm charts are available in `deployment/charts/flaskr/` (referenced in `pyproject.toml`).
