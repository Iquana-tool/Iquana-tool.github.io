# Calibrate to physical units

**You need:** the `curator` dataset role or higher. Calibration changes what every
stored measurement *means*, which is why it is not bundled with annotation work —
see [Roles and permissions](../concepts/roles.md#why-calibration-and-metadata-sit-at-curator-not-annotator).

Until an image is calibrated, its measurements are in **pixels**. Read
[Calibration](../concepts/calibration.md) for the concept.

## Steps

1. Switch to **Calibrate mode** and open the calibration drawer.
2. Start a scale measurement from that calibration's drawer button.
3. Draw the known distance across a reference in the image — a scale bar, a
   ruler, a calibration target.
4. Enter what that distance is in physical units.
5. Confirm. Object statistics should now report in your unit rather than in
   pixels.

++esc++ cancels a measurement in progress.

<figure class="iq-media">
  <video poster="../../assets/media/calibration.png" autoplay muted loop playsinline preload="none">
    <source src="../../assets/media/calibration.webm" type="video/webm">
    <source src="../../assets/media/calibration.mp4" type="video/mp4">
  </video>
  <figcaption>Measure-scale across a scale bar → enter the real distance → object stats flip from px to mm.</figcaption>
</figure>

## Per-dataset defaults

Calibrating every image by hand does not scale, and for a consistent acquisition
setup it is redundant. Set a **dataset default** when every image was captured at
the same working distance with the same optics; individual images can still
override it.

!!! warning "Calibrate before you quantify at scale"
    Metrics computed before calibration are in pixels. Recalibrating afterwards
    is supported — measurements are also stored pixel-natively, so nothing has to
    be re-derived from the imagery — but it is far less confusing to establish the
    scale first.

**Next:** [Quantify and export](quantify-and-export.md)
