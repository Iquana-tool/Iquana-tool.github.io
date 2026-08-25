# Services and ports

`./iquana.sh status` shows what is running, on which port, and at which commit.

<figure>
--8<-- "assets/img/architecture.svg"
<figcaption>The eight processes and how they reach each other. Everything except
your browser runs on the machine you installed on.</figcaption>
</figure>

| Service | What it does | Default port |
|---|---|---|
| `frontend` | the web UI you annotate in | 3000 |
| `backend` | REST API, database, exports | 8000 |
| `ai-service` | model inference for all AI-assisted tasks | 8004 |
| `ai-worker` | Celery worker for model training | — |
| `backend-worker` | Celery worker for batch inference runs | — |
| `mlflow` | model and experiment tracking | 5000 |
| `postgres` | the database (container) | 5432 |
| `redis` | task broker for both workers (container) | 6379 |

Logs are written to `logs/`, one file per service.

## Containers

`postgres` and `redis` run as containers and **cannot** start without a container
runtime. The installer creates:

- the volume `iquana-pg-data` — the database
- the containers `iquana-pg` and `iquana-redis`

These are the only things installed outside the `iquana-tool/` directory.

## Changing ports

If a port is already in use, the installer warns and lets you pick another one.
To change ports later:

```bash
./install.sh --reconfigure
```
