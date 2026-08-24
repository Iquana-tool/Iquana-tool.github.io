# Quantify and export

**You need:** the `reviewer` dataset role or higher to export annotations and
quantification; `curator` to export images.

## Before you start

- The objects you want measured are annotated and labelled.
- The images are [calibrated](calibrate.md), unless pixels are genuinely what you
  want.

## Steps

1. Open the dataset's quantification page.
2. **Choose a quantification profile** — which metrics get computed. See the
   [metric reference](../reference/metrics.md); computing metrics nobody will read
   costs time for nothing.
3. Explore the results: summary cards for the dataset, distributions, and the
   label tree.
4. **Drill down** to per-image and per-object values to sanity-check before you
   trust the aggregate.
5. **Export** the measurements for your own analysis.

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>quantify-explore</code></strong><br>
  Profile selector → summary cards → a distribution → per-image drilldown →
  download the report.<br>
  15–20 s · dark theme · 1280×800</span>
</div>

## Reading the output honestly

!!! warning "Missing is not zero"
    The contextual metrics (`nn_distance`, `mean_knn_distance`) **omit**
    contours that have no siblings, because a nearest-neighbour distance is
    undefined for them. A missing value there is not a distance of zero. By
    contrast `n_children` **is** defined for every contour, and a `0` there is a
    real count.

!!! note "Units follow calibration"
    Length metrics come out in the image's physical unit, area metrics in that
    unit squared, and ratio / count / colour / intensity metrics are unaffected.
    An uncalibrated image reports pixels.
