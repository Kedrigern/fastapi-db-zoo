# FastAPI with Database and Tests Example

This is a simple FastAPI project showcasing a clean structure with examples of using:
- [Pydantic](https://docs.pydantic.dev) for data validation and parsing.
- [FastAPI](https://fastapi.tiangolo.com) for building modern high-performance APIs.
- [SQLModel](https://sqlmodel.tiangolo.com/) for interacting with the database. Combines the best of SQLAlchemy and Pydantic for database interactions.
- [pytest](https://docs.pytest.org) for testing.
- [uv](https://docs.astral.sh/uv) for running commands efficiently.

The project demonstrates a basic API for managing **pets** and their **kinds**.

## Features

- A minimal structure for FastAPI projects.
- Integration with SQLModel for easy database management.
- Examples of testing using pytest.
- Quick setup and running instructions.

## Installation and run

Before you begin, make sure you have `uv` installed.

Start the FastAPI application:
```bash
uv run fastapi dev src/app.py
```

The API will be available at `http://localhost:8000`.

Explore the documentation:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Running Tests

```bash
uv run pytest
```