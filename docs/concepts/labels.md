# Label hierarchy

Labels in IQUANA nest into parent–child trees rather than sitting in a flat list.

## Why nesting matters

The usual failure mode of a flat label space is that you learn something halfway
through annotating. You started with `coral`, and now you need to distinguish
genera. In a flat scheme that means either re-annotating everything, or
maintaining `coral`, `coral_acropora`, `coral_porites` as unrelated strings that
only a human knows are related.

With a hierarchy, `acropora` is added *under* `coral`. Everything already
annotated as `coral` stays valid and stays queryable as `coral`; the new
annotations are simply more specific. **A class can be refined without discarding
the annotations above it.**

The hierarchy is also what makes parent–child object relationships meaningful —
see [Objects and annotations](objects.md) and the `n_children` metric in the
[metric reference](../reference/metrics.md).

## Ordering

The hierarchy is not only descriptive. [Batch inference](../guides/batch-inference.md)
walks the label tree in order, so parents are segmented before the children that
are searched for inside them.

## The LLM assistant

If an [LLM API key](../getting-started/configuration.md#llm-api-key) is
configured, IQUANA can draft a hierarchy from a description of your domain. It is
a starting point to edit, not an authority — it has no knowledge of your imagery,
only of your description.

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>label-hierarchy</code></strong><br>
  Nest a child under a parent; re-label an object to the child; show the parent's
  annotations still intact. Optionally the LLM draft.<br>
  10–14 s · dark theme · 1280×800</span>
</div>

## Naming

Label names are unique across the whole dataset, not merely among siblings. Two
different parents cannot both have a child called `edge` — pick names that are
unambiguous on their own.
