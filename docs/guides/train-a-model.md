# Train a model

**You need:** the `curator` dataset role or higher.

Fine-tune on the annotations you have corrected, so the next pass through the
loop starts from a better model.

## Steps

1. Open the dataset's training page and start a training run.
2. Configure the run and submit it. Training is queued to the `ai-worker` Celery
   worker, so you can leave the page.
3. Watch the job card for progress.
4. When it finishes, the run, its metrics and the resulting model version are
   tracked in **MLflow** (port 5000 by default) and registered for reuse.

The registered model then becomes selectable in
[batch inference](batch-inference.md) and in the model zoo.

<figure class="iq-media">
  <video poster="../../assets/media/training-run.png" autoplay muted loop playsinline preload="none">
    <source src="../../assets/media/training-run.webm" type="video/webm">
    <source src="../../assets/media/training-run.mp4" type="video/mp4">
  </video>
  <figcaption>Training modal → submit → job card progressing → resulting metrics / registered version.</figcaption>
</figure>

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>model-zoo</code></strong><br>
  Master-detail: model list → detail panel → sort by a performance stat → preview chips.<br>
  12–16 s · dark theme · 1280×800</span>
</div>

!!! tip "Train on corrected annotations, not raw predictions"
    Because model output stays separable from human edits, you can tell the
    difference. Fine-tuning on the model's own unreviewed output teaches it its
    own mistakes.

!!! note "Training without a GPU is impractical"
    It will run on the CPU, but not at a speed that supports iteration. See
    [GPU and CUDA](../operations/gpu.md).
