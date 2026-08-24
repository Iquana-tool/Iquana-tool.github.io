# Run batch inference

**You need:** the `curator` dataset role or higher.

Batch inference runs segmentation across a whole dataset in the background,
instead of image by image.

## Steps

1. Open the dataset's inference page.
2. **Assign a model per label.** You are not restricted to one model for the
   whole dataset — different classes can be served by different models.
3. **Choose the write mode** — see below.
4. Start the run, and watch the progress panel. The work is queued to a Celery
   worker, so you can leave the page.

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>batch-inference</code></strong><br>
  Per-label model planner → write mode → start → progress panel running.<br>
  14–18 s · dark theme · 1280×800</span>
</div>

## Patch vs. replace

| Mode | What it does |
|---|---|
| **Patch** | adds the run's predictions alongside what is already there |
| **Replace** | removes existing annotations in scope and writes the run's output instead |

!!! danger "Replace discards existing annotations"
    Including corrected ones. If a review pass has already happened on this
    dataset, replacing throws that work away. The UI warns before it does this —
    read the warning rather than clicking through it.

## Ordering follows the label hierarchy

The work list is ordered by your [label hierarchy](../concepts/labels.md), so
parents are segmented before the children searched for inside them. If your
hierarchy is wrong, the run order will be too.

**Next:** [Review and correct](review-and-correct.md)
