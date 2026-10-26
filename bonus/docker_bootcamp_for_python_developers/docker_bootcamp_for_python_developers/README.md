# Docker Bootcamp for Python Developers

## Contents
- `docker_bootcamp_for_python_developers.ipynb`: 30 lessons with Markdown explanations and code/command examples.
- `docker_practice_project/`: small Flask + Redis app with Dockerfile, Compose configuration, a health check, non-root user, and a named Redis volume.

## Prerequisites
Install Docker Desktop or Docker Engine + the Compose plugin.

## Start the practice app
Open a terminal in `docker_practice_project/` and run:

```bash
docker compose up --build
```

Browse to `http://localhost:5000/`, `/health`, and `/visits`.

`docker compose down` stops the app and removes containers/network while preserving named volumes. `docker compose down -v` also deletes the volume and stored data.

The notebook displays commands rather than executing them automatically. Review commands before running them in your own environment.
