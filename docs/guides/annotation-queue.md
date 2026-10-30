# Build an annotation queue

**You need:** the `annotator` dataset role or higher.

An annotation queue is the order you work through a dataset's images in. You build it
on the **Annotation** card before the editor opens; it is saved for you and this dataset,
so coming back resumes it. A scan counts as one item: its frames stay together.

## Choosing an order

| Sort images by | Puts first | Needs |
|---|---|---|
| **As uploaded** | the first (or last) images added | nothing |
| **Random** | a shuffle, fixed until you rebuild | nothing |
| **Diversity** | images least like anything already annotated | an embedding model |
| **Density** | typical images, ones that look like many others | an embedding model |
| **Uncertainty** | images where a model trained on this dataset is most torn | a trained model |

Diversity and Uncertainty are *active learning* orderings: they put the images that
teach a model the most early, so a model trained after the first batch is better than
one trained on images taken in upload order.

**Round robin** alternates two orderings, one image from each in turn.

## Taking turns by metadata

Pick a metadata key under **Take turns by**, e.g. `species`, and the queue takes one image
of each species in turn, every species keeping the order you chose. Nobody ends up
annotating one species to the end before the next. Images without the key form their own
group.

## Filtering

Search a metadata key under **Filter by** and narrow it to the values you want. Values of
one key are OR-ed, different keys are AND-ed, as in the gallery.

**Model confidence below** appears once a model trained on this dataset exists: it keeps
images whose most confident detection is below the threshold.

## Preparing

Diversity, Density and Uncertainty need data that is computed once and then reused: a
vector per image, or a trained model's detections. The first build fills what is missing
in the background and shows its progress.

- **Stop preparing** stops the job you started.
- Someone else asking for the same preparation waits on the same job. Closing the window,
  or stopping a job someone else started, only stops *your* waiting; the job carries on,
  and what it computed is used by the next build.

Scoring runs the trained model like [batch inference](batch-inference.md) does, so it
needs Batch inference to be switched on for the dataset.
