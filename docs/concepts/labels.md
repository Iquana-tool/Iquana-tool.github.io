# Label hierarchy

Labels in IQUANA nest into parent–child trees rather than sitting in a flat list.

## Nesting means "part of"

A child label is **a part of** its parent — not a kind of it. `nucleus` nested
under `cell` reads *a nucleus is part of a cell*; `polyp` under `colony` reads *a
polyp is part of a colony*. If you cannot say "a X is part of a Y" out loud, X
does not belong under Y.

This is not a stylistic preference. The label tree is the schema that object
nesting is validated against: **an object may only carry a label that is a direct
child of the label on the object containing it.** A contour labelled `nucleus`
can be drawn inside a contour labelled `cell` precisely because `nucleus` sits
under `cell` in the tree. Get the tree wrong and the annotation you want becomes
unsavable.

<figure>
--8<-- "assets/img/label-hierarchy.svg"
<figcaption>One label tree, two levels of containment deep. The tree declares
what may be annotated inside what.</figcaption>
</figure>

So the hierarchy is what makes parent–child *object* relationships meaningful —
see [Objects and annotations](objects.md) and the `n_children` metric in the
[metric reference](../reference/metrics.md).

## What nesting is not

It does not express subtypes. `acropora` is not part of `coral`, it *is a* coral,
so it does not belong nested underneath it — keep such classes as siblings at the
same level. IQUANA has no way to record "is a kind of" yet; it is planned as an
attribute rather than as a second meaning for nesting.

Sibling labels should be mutually exclusive: one object is a `nucleus` or a
`membrane`, never both. Nothing stops you from drawing two objects that overlap
geometrically — [that is supported](objects.md#overlapping-objects) — but a
single object carrying two sibling labels is not a thing the model can express.

## Ordering

The hierarchy is not only descriptive. [Batch inference](../guides/batch-inference.md)
walks the label tree in order, so containers are segmented before the parts
searched for inside them.

## The LLM assistant

If an [LLM API key](../getting-started/configuration.md#llm-api-key) is
configured, IQUANA can draft a hierarchy from a description of your domain. It is
a starting point to edit, not an authority — it has no knowledge of your imagery,
only of your description.

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>label-hierarchy</code></strong><br>
  Nest a part under its container; draw the part inside the container object;
  show the containment being accepted. Optionally the LLM draft.<br>
  10–14 s · dark theme · 1280×800</span>
</div>

## Naming

Label names are unique across the whole dataset, not merely among siblings. Two
different parents cannot both have a child called `edge` — pick names that are
unambiguous on their own.
