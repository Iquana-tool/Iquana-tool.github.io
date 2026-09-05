# Install

One installer sets up every IQUANA component on your machine.

```bash
git clone https://github.com/Iquana-tool/iquana-tool.git
```

```bash
cd iquana-tool && ./install.sh
```

The installer asks for the release channel, the ports, whether to install with
CUDA support, and your HuggingFace token. It then clones the component
repositories, wires their configuration together, installs all dependencies and
offers to start the tool.

!!! note "The first run takes a while"
    Several GB of Python packages and model weights are downloaded. This is
    normal, and only happens once.

When it finishes, IQUANA is at **<http://localhost:3000>**.

## Prerequisites

| Requirement | Why it is needed | Install |
|---|---|---|
| **git** | fetching the component repositories | <https://git-scm.com/downloads> |
| **uv** ≥ 0.10 | Python environments for the backend and the AI service | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| **bun** | the React frontend | `curl -fsSL https://bun.sh/install \| bash` |
| **Docker** | PostgreSQL and Redis run as containers and **cannot** start without a container runtime | <https://docs.docker.com/get-docker/> |

Podman is accepted as a drop-in replacement for Docker.

!!! warning "uv must be 0.10 or newer"
    Versions below 0.10 reject the PyTorch wheels the AI service needs. If the
    installer stops with *"uv is too old"*, run `uv self update`.

### Platform support

The installer is written for Linux and macOS. **On Windows, run it inside
WSL 2** — not in PowerShell or Git Bash.

### GPU

An NVIDIA GPU is optional but strongly recommended. Without one, model inference
and training run on the CPU, which is slow enough to change how you work. See
[GPU and CUDA](../operations/gpu.md).

## Installer options

```
./install.sh                 interactive install or update
./install.sh --reconfigure   go through the configuration questions again
./install.sh --yes           accept every stored/default answer, no prompts
./install.sh --no-start      set everything up, but do not start the services
```

<div class="iq-cast" data-cast="../../assets/media/install.cast"></div>

<figcaption class="iq-caption">
A real install, recorded with <code>asciinema</code>. The text is selectable —
you can copy any command straight out of the terminal above.
</figcaption>

## What gets installed where

The installer clones the components as sibling directories inside the
repository:

```
iquana-tool/
├── install.sh            setup and updates
├── iquana.sh             start / stop / status / logs
├── iquana.conf           your answers (secrets, gitignored)
├── backend/              REST API, database models, exports
├── frontend-react/       the web UI
├── ai-service/           unified AI service (inference + training)
├── logs/                 one log file per service
└── .mlflow/              MLflow tracking database and artifacts
```

Nothing is installed outside this directory except the container volume
`iquana-pg-data` (the database) and the containers `iquana-pg` and
`iquana-redis`.

## Next

- [First run](first-run.md) — create an account and annotate something
- [Configuration](configuration.md) — ports, hostnames, tokens
