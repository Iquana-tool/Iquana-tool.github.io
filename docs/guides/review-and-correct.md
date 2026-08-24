# Review and correct

**You need:** the `reviewer` dataset role or higher.

Review and correction are separate jobs on purpose — read
[Review and correction](../concepts/review.md) for why.

## Setting up a review queue

1. Open the dataset's review page and configure a queue.
2. **Pick a sort strategy** — the order objects are presented in. Confidence-based
   orderings put the model's least certain output first, which is where reviewer
   time changes the most.
3. Create the queue. It is a **snapshot**: a fixed list in a fixed order, so it
   has a definite end and does not reshuffle underneath you.

## Reviewing

Work through the queue giving each object a verdict. ++r++ rejects in review mode.

Rejected objects resolve as one of:

| Resolution | Meaning |
|---|---|
| **fixed** | it was wrong, and it has been corrected |
| **wont_fix** | it was wrong, and it is being left that way deliberately |

!!! info "`wont_fix` is a real answer"
    Recording that a human looked and chose not to change something is different
    from nobody having looked. That difference is what lets you state the
    annotation quality of a dataset later.

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>review-queue</code></strong><br>
  Setup → sort strategy → session → one <em>fixed</em>, one <em>wont_fix</em> →
  queue progress.<br>
  14–18 s · dark theme · 1280×800</span>
</div>

## Correcting

The correction pass is where rejected objects get fixed, using the same
[drawing and editing tools](draw-and-refine.md) as annotation. Model output stays
separable from human edits throughout, so a corrected annotation knows it was
corrected and by whom.

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>correction-pass</code></strong><br>
  Correction queue → fix a bad contour → model output vs. human edit distinguishable.<br>
  10–14 s · dark theme · 1280×800</span>
</div>

**Next:** [Train a model](train-a-model.md) on what you just corrected.
