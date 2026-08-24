# Create a dataset

**You need:** the `member` global role or higher (to create datasets at all).
See [Roles and permissions](../concepts/roles.md).

A dataset is the unit everything hangs off — images, labels, annotations,
profiles and membership. Read [Datasets and metadata](../concepts/datasets.md)
before you create your second one; the shape you choose is hard to change later.

## Steps

1. **Create the dataset.** From the datasets page, create a new one and give it a
   name that describes the *measurement question*, not the folder it came from.
2. **Define the metadata fields** you will want to filter and group by — site,
   depth, capture date, treatment. Do this **before** bulk upload; adding a field
   later means backfilling it across every image.
3. **Upload the images.**
4. **Fill in the metadata**, and check that the gallery filters behave the way
   you expect.

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>dataset-upload</code></strong><br>
  Create → upload → typed metadata → filter and group the gallery.<br>
  10–14 s · dark theme · 1280×800</span>
</div>

!!! tip "One dataset per measurement question"
    If two sets of images will never be compared to each other, they are two
    datasets. Label names are unique dataset-wide, so a single dataset is a single
    shared vocabulary.

**Next:** [Build a label hierarchy](build-a-label-hierarchy.md)
