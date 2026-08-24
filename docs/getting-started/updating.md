# Updating

Re-run the installer.

```bash
./install.sh
```

It checks every repository for new commits, shows you what changed, and asks
before applying anything or restarting the running services.

!!! tip "Your local work is safe"
    Checkouts with uncommitted local changes are left untouched, so you can
    develop inside `backend/` or `frontend-react/` without the installer
    overwriting your work.

## Stable vs. dev

| Channel | What it tracks | Who it is for |
|---|---|---|
| **stable** | the `main` branch of every repository | **This is what you want.** |
| **dev** | the `dev` branch where a repository has one, `main` otherwise | Newer features, but expect breakage. |

Switch channels with:

```bash
./install.sh --reconfigure
```

## After an update

If a service will not come back up, check its log first:

```bash
./iquana.sh logs ai-service
```

The AI service in particular can take a few minutes to start while it downloads
model weights. More in [Troubleshooting](../operations/troubleshooting.md).
