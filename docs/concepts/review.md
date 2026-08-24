# Review and correction

Review and correction are two different jobs, and IQUANA keeps them separate.

- **Review** asks *is this right?* — a verdict on existing annotations.
- **Correction** is the work of *making it right* — editing the ones that are not.

Splitting them means a reviewer can go through a hundred predictions quickly
without switching into drawing mode for each one, and the corrections can be done
in a focused pass afterwards, possibly by someone else.

## Queues are snapshots

A review queue is a **snapshot** taken when the queue is created — a fixed list
of objects, in a fixed order.

This matters more than it sounds. A live query would reshuffle under the
reviewer as annotations changed around them, making "how far through am I?"
unanswerable and making two reviewers' work impossible to compare. A snapshot is
a stable unit of work with a definite end.

## Ordering

Queues are built with a **sort strategy** — the order in which objects are
presented. The strategies are a registry rather than a fixed list, which is what
allows active-learning orderings: surface the objects the model was least
confident about first, so reviewer time goes where it changes the most.

## Verdicts

A reviewed object ends in one of two resolutions:

| Resolution | Meaning |
|---|---|
| **fixed** | it was wrong, and it has been corrected |
| **wont_fix** | it was wrong, and it is being left that way deliberately |

`wont_fix` is not a shrug. Recording that a human looked at something and chose
not to change it is different from nobody having looked, and the difference
matters when you later ask what the annotation quality of a dataset actually is.

## Provenance

Model output stays separable from human edits throughout. A corrected annotation
knows it was corrected, and by whom — see [Roles and permissions](roles.md) for
how attribution works across a team.

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>review-queue</code></strong><br>
  Review setup → pick a sort strategy → session → one <em>fixed</em>, one
  <em>wont_fix</em> → progress through the queue.<br>
  14–18 s · dark theme · 1280×800</span>
</div>

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>correction-pass</code></strong><br>
  Correction queue → fix a bad contour → model output vs. human edit staying distinguishable.<br>
  10–14 s · dark theme · 1280×800</span>
</div>
