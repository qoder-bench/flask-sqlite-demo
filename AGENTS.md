# Flask SQLite demo

## Tech Stack

- Python 3.13
- Project/Package Manager: [uv](https://docs.astral.sh/uv)
- Web Framework: Flask
- Database: SQLite
- ORM: Flask-SQLAlchemy
- Testing: pytest
- Linter: [ruff](https://github.com/astral-sh/ruff)
- type checker: [ty](https://github.com/astral-sh/ty)

## Project structure

- `db/demo.sqlite3`: SQLite database file
- `db/schema.ddl`: database schema
- `app/`: Main application code
    - `main.py`: Entry point of the application
    - `router/`: Blueprint definitions
    - `domains/`: Domain related code
        - `models.py`: SQLModel models
        - `repository/`: Repository layer
- `tests/`: integration test for the application

For unit test, please put them in project's `/tests` directory.

## Build

The project uses [just](https://github.com/casey/just) as task runner.

- Start server: `just start`
- Generate SQLModels: `just gen-sqlalchemy`

## Python Guide Line

* Modern Python 3.13 with full type hints
* Proper error handling and logging
* Clean architecture with SOLID principles

## Configurations

The project use `.env` file to store configurations.