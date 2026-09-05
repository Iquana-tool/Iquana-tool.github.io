# Build a label hierarchy

**You need:** the `curator` dataset role or higher (label management).

You cannot save an annotation without a label. Labels nest, and nesting means
*part of* — read [Label hierarchy](../concepts/labels.md) for why that matters.

## Steps

1. **Start with the containers.** Define the whole objects first — the things
   that other things sit inside. These are your top-level labels.
2. **Nest each part under the thing it is part of.** Say it out loud before you
   nest: *a nucleus is part of a cell*. If the sentence does not work, the label
   belongs at the top level instead.
3. **Rearrange when you learn better.** Drag a label onto the label it is a part
   of, or drop it below the tree to make it a whole object again. The move action
   on the row does the same thing from a dialog. If objects are already annotated
   in a way the move would break, you are told how many before anything changes —
   see [Rearranging later](../concepts/labels.md#rearranging-later).
4. **Check the order.** [Batch inference](batch-inference.md) walks the tree in
   order, so containers are segmented before the parts searched for inside them.

## Using the LLM assistant

If an [LLM API key](../getting-started/configuration.md#llm-api-key) is
configured, IQUANA can draft a hierarchy from a description of your domain.

Treat the draft as a starting point to edit. It knows your description, not your
imagery.

<figure class="iq-media">
  <video poster="../../assets/media/label-hierarchy.png" autoplay muted loop playsinline preload="none">
    <source src="../../assets/media/label-hierarchy.webm" type="video/webm">
    <source src="../../assets/media/label-hierarchy.mp4" type="video/mp4">
  </video>
  <figcaption>Nest a part under its container → draw the part inside the container object → the containment is accepted. Optionally the LLM draft.</figcaption>
</figure>

!!! warning "Nesting is not for subtypes"
    `acropora` is a kind of `coral`, not a part of one, so it does not belong
    nested under it. Keep subtypes as siblings at the same level — IQUANA cannot
    record "is a kind of" yet.

!!! warning "Label names are unique dataset-wide"
    Not merely among siblings. Two different parents cannot both have a child
    called `edge`.

!!! danger "Deleting a label cascades"
    Deleting a label removes it from every contour carrying it. This is why label
    management sits at the curator role.

**Next:** [Annotate with AI](annotate-with-ai.md)
