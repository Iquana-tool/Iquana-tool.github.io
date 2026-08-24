# Contributing

## Reporting bugs and requesting features

Please use the
[issue templates](https://github.com/Iquana-tool/iquana-tool/issues/new/choose).

The `iquana-tool` repository is the tracker for **all** of IQUANA — bug reports
and feature requests for the frontend, the backend, the AI service and the
installer all belong there.

- **For bugs**, steps to reproduce and a screenshot help enormously.
- **For feature requests**, a sketch or mockup does.

We are a small research team and cannot promise to implement every request.

## Working on the code

The installer clones each component as a sibling directory inside `iquana-tool/`.
Checkouts with **uncommitted local changes are left untouched** by the installer,
so you can develop inside `backend/` or `frontend-react/` without your work being
overwritten by an update.

If you want to track unreleased work, switch to the `dev` channel:

```bash
./install.sh --reconfigure
```

See [Updating](../getting-started/updating.md#stable-vs-dev) for what that
channel means.

## Collaborations

If you would like to bring IQUANA to your own domain, write to
[robert.leist@dfki.de](mailto:robert.leist@dfki.de).
