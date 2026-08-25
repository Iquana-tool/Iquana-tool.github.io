# Metrics

Every metric in the registry, grouped by [tier](../concepts/quantification.md#metric-tiers).
Which of them get computed for a dataset is decided by its
[quantification profile](../concepts/quantification.md#quantification-profiles).

**Unit kind** says how [calibration](../concepts/calibration.md) affects the
value: `length` metrics come out in the image's physical unit, `area` metrics in
that unit squared, and `ratio` / `count` / `colour` / `intensity` metrics are
unaffected by it.

## Geometry

Computed from the contour alone.

<figure>
--8<-- "assets/img/metric-explainer.svg"
<figcaption>The four geometry metrics on one contour. The dashed chord is the
genuinely farthest pair of points on this outline, and 0.70 is its real
circularity — both are computed from the shape drawn, not sketched.</figcaption>
</figure>

| Key | Name | Unit kind | Description |
|---|---|---|---|
| `area` | Area | area | Enclosed area of the contour polygon. |
| `perimeter` | Perimeter | length | Closed perimeter (arc length) of the contour polygon. |
| `circularity` | Circularity | ratio | Dimensionless shape descriptor `4·π·area / perimeter²` — **1.0 for a circle**, lower for elongated or ragged outlines. |
| `max_diameter` | Max Diameter | length | Maximum distance between any two points of the contour. |

## Appearance

Computed from the contour **and the image pixels**, so these go stale when the
underlying imagery or the outline changes.

| Key | Name | Unit kind | Description |
|---|---|---|---|
| `mean_color_rgb` | Mean color (RGB) | colour | Mean red, green and blue channel value (0–255 each) over the contour's interior. |
| `mean_color_lab` | Mean color (CIELAB) | colour | Mean CIELAB colour, using OpenCV's 8-bit scaling (L, a, b each in 0–255). |
| `mean_intensity` | Mean intensity | intensity | Mean grayscale luminance (0–255), via OpenCV's standard conversion. |

## Contextual

Computed from the contour **and the other contours around it**. A contextual
value on one object goes stale when a *neighbour* moves, even if that object's own
outline never changed.

| Key | Name | Unit kind | Description |
|---|---|---|---|
| `nn_distance` | Nearest-neighbour distance | length | Euclidean distance from this contour's centroid to the centroid of the nearest **other** contour sharing the same parent. |
| `mean_knn_distance` | Mean distance to 3 nearest neighbours | length | Mean euclidean distance from this contour's centroid to its up-to-3 nearest same-parent sibling centroids (fewer if the group is smaller). |

!!! warning "Only-child contours are omitted, not zero"
    Both contextual metrics need at least one sibling. A contour with no siblings
    has no meaningful neighbour distance, so it is **omitted from the result
    entirely** rather than reported as `0`. Do not read a missing value as a
    distance of zero.

!!! info "Who counts as a sibling"
    Contours sharing the same parent. **Root-level contours are siblings of every
    other root-level contour in the image.**

!!! note "k is fixed at 3"
    `mean_knn_distance` uses k = 3, and this is not currently configurable.

## Relational

Computed from the contour **and its children**.

| Key | Name | Unit kind | Description |
|---|---|---|---|
| `n_children` | Number of children | count | Number of contours in the same image that name this contour as their parent — how many direct child objects it contains. |

!!! info "Zero is a real value here"
    Unlike the contextual metrics, `n_children` is defined for **every** contour:
    a leaf object with no children has value `0`, which is a meaningful count
    rather than a missing value. No contour is omitted.

## Extending the registry

The registry is extensible — a metric is a class that declares a `key`, `name`,
`description`, `tier` and `unit_kind` and implements a batch compute. Adding one
does not require a schema change, because measurements are stored in a tall table
keyed by `(contour_id, metric_key)` rather than as columns.
