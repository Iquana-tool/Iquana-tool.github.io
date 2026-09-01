# Objects and annotations

An **object** is one annotated thing in one image: a closed contour, a label, and
the provenance of how it came to exist.

## Contours

An object's geometry is a closed contour — a polygon in image coordinates. It can
come from:

- a **model prediction**, from a point/box/polygon/freehand prompt
- a **manual drawing**, with the polygon or freehand tools
- a **model prediction that a human then edited**

That last case is the common one, and it is why provenance is tracked rather than
inferred. Model output and human edits stay separable, which matters both for
trusting a measurement and for deciding what to fine-tune on.

## Parents and children

Objects can name another object in the same image as their parent. This is what
lets you count polyps within a colony, or measure the area of a structure and the
structures inside it, and it is what the `n_children` metric reads.

Parent–child links between *objects* are a different thing from parent–child
links between *labels*. The [label hierarchy](labels.md) declares which kinds of
thing may contain which; object parentage records which particular things
actually do. The two are tied together by one rule: an object's label must be a
direct child of the label on its parent object.

## Overlapping objects

Multiple objects may overlap on the same image. Dense, overlapping structure was
one of the driving cases for the tool — reef survey imagery where colonies touch
and occlude one another — so overlap is a supported state rather than a conflict
to resolve.

## Editing

Any contour can be edited after the fact: select it (++v++), press ++e++, and
adjust its points directly — you do not have to redraw an outline to fix part of
it.

!!! note "Brush / mask painting"
    The rail has a **Brush / mask** slot (++m++), but it is **not available in
    this build** — it renders disabled rather than silently missing. Refine
    contours by editing their points instead.

See [Draw and refine manually](../guides/draw-and-refine.md).

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>contour-edit</code></strong><br>
  Select a predicted contour, enter edit mode, adjust its points at high zoom.<br>
  10–12 s · zoomed in on fine detail · dark theme · 1280×800</span>
</div>
