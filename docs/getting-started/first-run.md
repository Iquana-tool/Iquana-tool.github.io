# First run

This page takes you from a freshly installed IQUANA to one measured object.

## 1. Start the services

```bash
./iquana.sh start
```

`./iquana.sh status` shows what is running, on which port, and at which commit.
If something is missing, its log is in `logs/` — see
[Command line](../reference/cli.md).

Open **<http://localhost:3000>**.

## 2. Create the first account

The **first** account can always be created, whether or not self-registration is
allowed — a fresh installation is never locked out of itself. Create it now; it
becomes the platform administrator.

If other people will use this installation, read
[Configuration → identifying your instance](configuration.md#identifying-your-instance)
before handing out the address, and decide deliberately whether strangers may
register themselves. Self-registration is **off** by default.

## 3. Create a dataset and upload images

A dataset is the unit everything else hangs off: images, labels, annotations,
quantification profiles and membership all belong to one dataset.

See [Create a dataset](../guides/create-a-dataset.md).

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>dataset-upload</code></strong><br>
  Create a dataset, upload images, add typed per-image metadata, filter the gallery by it.<br>
  10–14 s · dark theme · 1280×800</span>
</div>

## 4. Define at least one label

You cannot save an annotation without a label to attach it to. Labels nest into
parent–child trees, so start with something coarse — you can refine it later
without discarding the annotations above it.

See [Build a label hierarchy](../guides/build-a-label-hierarchy.md).

## 5. Annotate one object

Open an image in the annotation workspace, pick the **Point** tool (++p++), click
on an object, and press ++enter++ to run the model on the prompt. Accept the
result and assign a label with ++l++.

The full prompt vocabulary — positive and negative points, boxes, polygons and
freehand — is in
[Annotate with AI](../guides/annotate-with-ai.md). Press ++question++ at any time
for the [keyboard shortcuts](../reference/shortcuts.md).

## 6. Calibrate, so the numbers mean something

Until you calibrate, every measurement is in pixels. Calibration maps pixels to a
physical length unit, and can be set per dataset when your acquisition setup is
consistent.

See [Calibrate to physical units](../guides/calibrate.md).

## 7. Quantify and export

With at least one labelled, calibrated object, the quantification page will
compute metrics for it and let you export the result.

See [Quantify and export](../guides/quantify-and-export.md) and the
[metric reference](../reference/metrics.md).

## Where to go next

You have been through the loop once. From here:

- **Scale it up** — [Run batch inference](../guides/batch-inference.md) across the
  whole dataset instead of image by image
- **Bring in other people** — [Manage access](../guides/manage-access.md)
- **Improve the model** — [Train a model](../guides/train-a-model.md) on your
  corrected annotations
