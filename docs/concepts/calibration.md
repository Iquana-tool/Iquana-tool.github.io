# Calibration

Until an image is calibrated, every measurement it produces is in **pixels**. A
pixel area is not a quantity anyone can compare across setups, publish, or
reason about physically. Calibration maps image space to a physical length unit
so that areas come out in mm², distances in mm, and ratios stay ratios.

## How it works

Calibration establishes a scale — how many physical units one pixel spans — and
an associated unit for the image. Once set, metrics are computed in that unit
rather than in pixels.

Internally, measurements are also stored in pixel-native form, so a
re-calibration does not require re-deriving geometry from scratch and a dataset
whose images share a unit can be aggregated consistently.

## Per image, per dataset

Setting a scale on every image by hand does not scale, and for a consistent
acquisition setup it is also redundant. Calibration therefore supports
**per-dataset defaults**: when every image was captured at the same working
distance with the same optics, calibrate once and let the dataset supply it.

Images captured differently can still override the default individually.

## Measuring a scale

Scale measurement belongs to **Calibrate mode**, and is started from that
calibration's drawer button — not from the annotation tool rail.

That is a deliberate placement: on the rail it invited an annotator to
recalibrate an image in the middle of annotating it, which silently rescales
every measurement already taken. Setting a scale is a calibration, so it lives
with the other calibrations and behind the
[curator permission](roles.md#why-calibration-and-metadata-sit-at-curator-not-annotator).

You draw a known distance across a reference in the image — a scale bar, a ruler,
a calibration target — and enter what that distance is in physical units. Press
++esc++ to cancel a measurement in progress.

## Units

The image's unit is what every length- and area-kind metric is reported in. See
the `unit_kind` column in the [metric reference](../reference/metrics.md):

- **length** metrics (perimeter, max diameter, neighbour distances) come out in the unit
- **area** metrics come out in the unit squared
- **ratio**, **count**, **colour** and **intensity** metrics are unaffected by calibration

<figure class="iq-media">
  <video poster="../../assets/media/calibration.png" autoplay muted loop playsinline preload="none">
    <source src="../../assets/media/calibration.webm" type="video/webm">
    <source src="../../assets/media/calibration.mp4" type="video/mp4">
  </video>
  <figcaption>Measure-scale tool across a scale bar → enter the real distance → object stats flip from px to mm.</figcaption>
</figure>

!!! warning "Calibrate before you quantify at scale"
    Metrics computed before calibration are in pixels. Calibrating afterwards is
    supported, but it is far less confusing to establish the scale first.
