# Draw and refine manually

**You need:** the `annotator` dataset role or higher (to edit your own
annotations), or `reviewer` and above to edit anyone's.

Not everything should be prompted. Small, low-contrast or heavily occluded
objects are often faster to draw than to argue with a model about.

## Drawing

- **Polygon** (++g++) — click points around the object, close the outline.
- **Freehand** (++f++) — trace the boundary in one gesture.

With the prompt action set to **Add** (++a++), a closed outline becomes an object
immediately. Otherwise press ++shift+enter++ to add the drawn outlines as objects.

## Editing an existing contour

1. Select it with ++v++.
2. Press ++e++ to enter edit mode.
3. Adjust the points directly.

This works the same on a model prediction as on something you drew — you do not
have to redraw an outline to fix part of it.

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>contour-edit</code></strong><br>
  Select a predicted contour → edit mode → adjust points at high zoom.<br>
  10–12 s · dark theme · 1280×800</span>
</div>

!!! note "Brush / mask painting is not available"
    The rail shows a **Brush / mask** slot (++m++), but there is no
    implementation in this build, so it renders disabled rather than silently
    missing. Refine by editing contour points instead.

## Fine detail

Zoom (++z++, or ++plus++ / ++minus++) and pan (++h++, or hold ++space++) are worth
learning properly — most of the real work in dense imagery happens zoomed in.
++0++ returns to fit-to-screen.

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>zoom-detail</code></strong><br>
  A dense, overlapping cluster; zoom in and refine one contour among its neighbours.<br>
  10–14 s · dark theme · 1280×800</span>
</div>
