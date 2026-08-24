# Configuration

All your answers are stored in **`iquana.conf`** next to the installer (mode
`600`, gitignored — it holds your tokens, the generated database password and the
signing key).

From it the installer generates the per-service configuration:

| File | Holds |
|---|---|
| `backend/.env` | database, Redis, MLflow and AI-service URLs, CORS origins, signing key, instance identity |
| `ai-service/.env` | HuggingFace token, Redis and MLflow URLs |
| `frontend-react/.env.local` | the API URL the browser calls, and the frontend's port |

To change something, either run `./install.sh --reconfigure` or edit
`iquana.conf` by hand and re-run `./install.sh`.

!!! warning "Editing the generated `.env` files directly works, but does not last"
    The next installer run replaces them, keeping a `.bak` copy. Put durable
    changes in `iquana.conf`.

## Identifying your instance

If other people will sign in to your installation, the installer can ask for a
name, a hosting organisation, and an address to request access from. All three
appear on the sign-in page — *"Welcome to HIFMB Reef Lab"*, *"hosted by …"*,
*"Request access from …"* — and all three are optional. Leave them empty and the
page simply reads as IQUANA.

The same section asks whether **self-registration** is allowed. It is **off by
default**, so an installation reachable from your network does not accept
strangers unless you say so; with it off, you create accounts and hand them out.
The *first* account can always be created either way.

??? info "Why these live in the backend's configuration, not the frontend's"
    Two reasons. The registration policy has to be enforced by the API — a
    sign-in page that merely hides the link is not a closed door. And Vite bakes
    frontend variables in at build time, which would mean rebuilding the frontend
    to correct a typo in your instance name.

    The sign-in page reads them from `GET /instance/` at runtime, so
    `./install.sh --reconfigure` followed by a backend restart is enough to
    change them.

## Serving IQUANA to other machines

Answer the installer's hostname question with the hostname or IP that *other*
machines use to reach the server, rather than `localhost`. That value goes into
the frontend's API URL and into the backend's allowed CORS origins.

## Optional integrations

### HuggingFace token

Needed for gated model weights (SAM, DINOv3, …). Create a **read** token at
<https://huggingface.co/settings/tokens>.

### LLM API key

Enables the *"describe your label space"* assistant, which drafts a label
hierarchy from a description of your domain. Any
[LiteLLM](https://docs.litellm.ai/docs/providers)-supported provider works; the
model is named `<provider>/<model>`, for example:

```
anthropic/claude-opus-4-8
ollama/llama3
```

## Ports

Defaults are listed in [Services and ports](../reference/services.md). If a port
is already in use, the installer warns and lets you pick another one. To change
ports later, run `./install.sh --reconfigure`.
