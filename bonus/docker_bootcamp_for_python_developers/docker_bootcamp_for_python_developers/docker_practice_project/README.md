# Docker Practice App: Flask + Redis

## Start
Open a terminal in this folder and run:

```bash
docker compose up --build
```

Then visit:
- http://localhost:5000/
- http://localhost:5000/health
- http://localhost:5000/visits

The `/visits` endpoint increments a Redis counter. Compose provides service discovery by service name (`redis`) and keeps Redis data in a named volume.

## Useful commands

```bash
docker compose ps
docker compose logs -f web
docker compose exec web sh
docker compose down
```

`docker compose down` removes the containers and project network but keeps the named volume. `docker compose down -v` also deletes the volume and its data.

This is a local learning app, not a production-ready internet-facing service.
