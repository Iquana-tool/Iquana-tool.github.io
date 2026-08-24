# Datasets and metadata

A **dataset** is the unit everything else hangs off. Images, labels,
annotations, quantification profiles, calibration defaults and membership all
belong to exactly one dataset.

This is deliberate. Label names are unique dataset-wide, so a label means one
thing everywhere inside a dataset, and a measurement can be compared across every
image in it without asking whether two people meant the same thing by "polyp".

## Images

Images are uploaded into a dataset and browsed in its gallery. Each image
carries:

- the pixel data itself
- **typed per-image metadata** you define
- a **calibration**, if one has been set — see [Calibration](calibration.md)
- the annotations drawn on it — see [Objects and annotations](objects.md)

## Typed metadata

Metadata fields are typed rather than free-form strings, which is what makes them
useful for filtering and grouping: a depth is a number you can range-filter, a
survey site is a category you can group by, a capture date is a date you can sort
on.

In practice this is what lets you ask questions of the *analysis* rather than of
individual images — "mean colony area by site" only works if "site" is a field
and not a naming convention buried in filenames.

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>dataset-metadata-filter</code></strong><br>
  Gallery filtered and grouped by a typed metadata field.<br>
  6–8 s · dark theme · 1280×800</span>
</div>

## Practical advice

- **One dataset per measurement question**, not per folder on disk. If two sets
  of images will never be compared to each other, they are two datasets.
- **Decide the metadata fields before bulk upload.** Adding a field later means
  backfilling it.
