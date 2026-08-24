# Command line

Two scripts, both at the root of the `iquana-tool` checkout.

## `iquana.sh` — run it

```bash
./iquana.sh start            # start everything
./iquana.sh stop             # stop everything
./iquana.sh restart          # stop, then start
./iquana.sh status           # what is running, on which port, at which commit
./iquana.sh logs backend -f  # follow one service's log
```

Every command also takes a list of services:

```bash
./iquana.sh restart ai-service ai-worker
```

Service names are listed in [Services and ports](services.md).

## `install.sh` — set it up and update it

```
./install.sh                 interactive install or update
./install.sh --reconfigure   go through the configuration questions again
./install.sh --yes           accept every stored/default answer, no prompts
./install.sh --no-start      set everything up, but do not start the services
```

Re-running `./install.sh` is also how you [update](../getting-started/updating.md):
it checks every repository for new commits, shows what changed, and asks before
applying anything or restarting running services.

Checkouts with uncommitted local changes are left untouched.
