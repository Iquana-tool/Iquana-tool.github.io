# Build a label hierarchy

**You need:** the `curator` dataset role or higher (label management).

You cannot save an annotation without a label. Labels nest — read
[Label hierarchy](../concepts/labels.md) for why that matters.

## Steps

1. **Start coarse.** Define the top-level classes you are certain about. You can
   refine them later without discarding what you have already annotated.
2. **Nest the refinements underneath** as you learn them.
3. **Check the order.** [Batch inference](batch-inference.md) walks the tree in
   order, so parents are segmented before the children searched for inside them.

## Using the LLM assistant

If an [LLM API key](../getting-started/configuration.md#llm-api-key) is
configured, IQUANA can draft a hierarchy from a description of your domain.

Treat the draft as a starting point to edit. It knows your description, not your
imagery.

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>label-hierarchy</code></strong><br>
  Nest a child under a parent → re-label an object to the child → the parent's
  annotations still intact. Optionally the LLM draft.<br>
  10–14 s · dark theme · 1280×800</span>
</div>

!!! warning "Label names are unique dataset-wide"
    Not merely among siblings. Two different parents cannot both have a child
    called `edge`.

!!! danger "Deleting a label cascades"
    Deleting a label removes it from every contour carrying it. This is why label
    management sits at the curator role.

**Next:** [Annotate with AI](annotate-with-ai.md)
