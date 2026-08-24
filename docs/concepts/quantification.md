# Quantification

Quantification turns annotated objects into numbers. Every metric is computed
**per object**, stored against that object, and stays traceable to it — which is
the point of carrying objects through the whole loop rather than exporting masks
and measuring them somewhere else.

## Metric tiers

Metrics are organised into four tiers by what a metric needs in order to be
computed. The tier is not cosmetic: it determines what invalidates a stored
value.

| Tier | Depends on | Examples |
|---|---|---|
| **Geometry** | the contour alone | area, perimeter, circularity, max diameter |
| **Appearance** | the contour **and the image pixels** | mean colour (RGB), mean colour (CIELAB), mean intensity |
| **Contextual** | the contour **and the other contours around it** | nearest-neighbour distance, mean distance to *k* nearest neighbours |
| **Relational** | the contour **and its children** | number of children |

Because the dependencies differ, so does staleness. Editing a contour's shape
invalidates its geometry. Moving *a neighbour* invalidates a contextual metric on
an object whose own outline never changed. Adding a child invalidates a
relational metric. IQUANA tracks this per tier and recomputes only what actually
went stale.

The full list, with keys, descriptions and unit kinds, is in the
[metric reference](../reference/metrics.md). The registry is extensible — adding
a metric is adding a class, not changing the schema.

## Quantification profiles

A **profile** selects which metrics to compute for a dataset. You rarely want all
of them: a morphology study needs geometry, a bleaching study needs appearance, a
spatial-distribution study needs contextual metrics, and computing the rest costs
time for numbers nobody will read.

Profiles are per dataset, so the choice is made once and applies consistently
across every image in it.

## Units

Metrics come out in the image's physical unit when it is
[calibrated](calibration.md), and in pixels when it is not. Values are also kept
in pixel-native form so that aggregation across a dataset stays consistent — and
so that recalibrating does not mean recomputing from the imagery again.

## Exploring the results

The quantification page presents summary cards, distributions and a label tree
for the dataset as a whole, and drills down to per-image and per-object values.
From there the measurements can be exported for your own analysis.

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>quantify-explore</code></strong><br>
  Profile selector → summary metric cards → a distribution → per-image drilldown →
  download the report.<br>
  15–20 s · dark theme · 1280×800</span>
</div>
