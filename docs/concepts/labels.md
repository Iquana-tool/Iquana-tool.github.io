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

Sibling labels are semantically disjoint: one object is a `nucleus` or a
`membrane`, never both, and a given piece of the image belongs to one semantic
object. That is a claim about meaning, not about geometry — two objects may still
[overlap in the image](objects.md#overlapping-objects), which is supported.

Where they do overlap, though, one of them is really behind the other, and
IQUANA has no way to record that: there is no depth axis, so the annotator has to
predict where the hidden boundary runs. Unless you need that guess, it is worth
avoiding.

## Rearranging later

A label can be moved under a different parent, or promoted back to the top level,
from the label management page — drag it onto the label it is a part of, or use the
move action on its row. While you drag, any destination that would cost you
annotations says so, with the number, before you let go. Because nesting is what annotation validates
against, a move can strand objects that were legal when they were drawn: an
object labelled `nucleus` inside a `cell` stops being legal the moment `nucleus`
becomes a part of something else.

IQUANA refuses such a move and tells you how many objects it would affect. You
can then accept the consequence explicitly, which **detaches** those objects —
they keep their label and stop being nested inside anything. The containment is
not restored by moving the label back, so it is worth checking the count before
confirming.

Moves that strand nothing — the common case, since a label space is usually
rearranged early — just happen.

## Ordering

The hierarchy is not only descriptive. [Batch inference](../guides/batch-inference.md)
walks the label tree in order, so containers are segmented before the parts
searched for inside them.

## The LLM assistant

If an [LLM API key](../getting-started/configuration.md#llm-api-key) is
configured, IQUANA can draft a hierarchy from a description of your domain. It is
a starting point to edit, not an authority — it has no knowledge of your imagery,
only of your description.

<figure class="iq-media">
  <video poster="../../assets/media/label-hierarchy.png" autoplay muted loop playsinline preload="none">
    <source src="../../assets/media/label-hierarchy.webm" type="video/webm">
    <source src="../../assets/media/label-hierarchy.mp4" type="video/mp4">
  </video>
  <figcaption>Nest a part under its container; draw the part inside the container object; show the containment being accepted. Optionally the LLM draft.</figcaption>
</figure>

## Naming

Label names are unique across the whole dataset, not merely among siblings. Two
different parents cannot both have a child called `edge` — pick names that are
unambiguous on their own.
