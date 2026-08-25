---
title: IQUANA documentation
---

# IQUANA documentation

**I**ntelligent **QU**antification, **AN**notation and **A**nalysis — a tool for
AI-assisted segmentation, annotation and quantification of scientific image
datasets, built at [DFKI](https://www.dfki.de/) in partnership with
[HIFMB](https://hifmb.de/).

Most annotation tools stop at the mask. IQUANA carries the same objects through
measurement and review, so what you export is an analysis rather than a pile of
polygons — and every number stays traceable to the object it came from.

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>hero-prompt-to-mask</code></strong><br>
  A point prompt lands on an object, the mask blooms in, it is accepted and labelled.<br>
  6–8 s · silent loop · dark theme · 1280×800</span>
</div>

## Where to start

<div class="iq-cards" markdown>

[**Install IQUANA**<span>One installer sets up every component. Linux and macOS directly, Windows via WSL 2.</span>](getting-started/install.md)

[**Understand the model**<span>Datasets, labels, objects, calibration, quantification — what the pieces mean.</span>](concepts/index.md)

[**Follow a guide**<span>Task-by-task walkthroughs, from your first dataset to an exported analysis.</span>](guides/index.md)

[**Look something up**<span>Keyboard shortcuts, the metric registry, services and ports, CLI commands.</span>](reference/index.md)

</div>

## The loop

IQUANA is built around a cycle rather than a labelling queue:

| | Step | What happens |
|---|---|---|
| 01 | **Upload** | Datasets with typed per-image metadata you can filter and group by. |
| 02 | **Predict** | Run segmentation models across a dataset, one model per label if you need it. |
| 03 | **Correct** | Review and correction queues surface what the model most likely got wrong. |
| 04 | **Quantify** | Per-object metrics in physical units, driven by configurable profiles. |
| 05 | **Export** | Measurements, provenance and label hierarchy out to your own analysis. |

Each pass through the loop improves the annotations, and the corrected
annotations are what you fine-tune the next model on.

## Getting help

- **Something is broken, or you want a feature** — please use the
  [issue templates](https://github.com/Iquana-tool/iquana-tool/issues/new/choose).
  Bug reports for the frontend, backend, AI service and installer all belong in the
  same tracker.
- **Something will not start** — begin with [Troubleshooting](operations/troubleshooting.md).
- **You want to bring IQUANA to your own domain**, or are interested in a research
  collaboration — write to [robert.leist@dfki.de](mailto:robert.leist@dfki.de).

We are a small research team and cannot promise to implement every request.
