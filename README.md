# Feature Flags Service

This project provides a small feature flag service built with **Django** and **Django REST Framework**. It exposes CRUD APIs to manage organisations, projects, environments and feature flags. Evaluations of flags are recorded and can be aggregated by a Celery task.

## Project Highlights

- **Django 5** with a custom `User` model.
- REST API with JWT authentication.
- Celery for background processing.
- PostgreSQL and Redis used in the default Docker setup.
- Demo seeding script for sample data.

## Local Development

1. Copy `.env.sample` to `.env.dev` and adjust values if needed.
2. Start the stack:

   ```bash
   docker compose up --build
   ```

   This brings up the Django app, Postgres and Redis.

3. Apply migrations:

   ```bash
   docker compose exec web python manage.py migrate
   ```

4. (Optional) Seed demo data:

   ```bash
   docker compose exec web python scripts/seed_demo.py
   ```

The API will be available at `http://localhost:8000/api/` and browsable docs at `http://localhost:8000/api/docs/`.

## Celery

A Celery worker and beat scheduler are included in `docker-compose.yml`. The task `core.tasks.aggregate_flag_evaluations` aggregates evaluation counts from the last 24 hours. In development it simply logs the results.

## Pre‑commit Hooks

Formatting and linting are configured with [Black](https://black.readthedocs.io/) and [Ruff](https://docs.astral.sh/ruff/). Install hooks with:

```bash
pre-commit install
```

Then hooks will run automatically on each commit, or you can run them on all files with `pre-commit run --all-files`.

## API Overview

The main endpoints are provided by DRF viewsets:

- `/api/organisation/`
- `/api/project/`
- `/api/environment/`
- `/api/featureflag/`

A JWT can be obtained via `/api/token/` and refreshed via `/api/token/refresh/`.

See the generated OpenAPI docs at `/api/docs/` for details on request and response formats.

