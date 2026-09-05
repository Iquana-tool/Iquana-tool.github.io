# Annotate with AI

**You need:** the `annotator` dataset role or higher.

The workspace puts a foundation segmentation model behind a set of prompts. You
tell it roughly where the object is; it produces the outline; you keep, adjust or
discard it.

## The prompt vocabulary

| Tool | Key | Use it for |
|---|---|---|
| **Point** | ++p++ | the fastest prompt — one click inside the object |
| **Bounding box** | ++b++ | when a point is ambiguous and you want to bound the search |
| **Polygon** | ++g++ | coarse enclosure of an awkward shape |
| **Freehand** | ++f++ | tracing a rough boundary by hand |

Prompts are **positive or negative**. A negative prompt says *"not this"* — it is
how you cut a neighbouring object out of a mask that grabbed too much, and it is
usually faster than editing the contour afterwards.

## Steps

1. Pick a tool and place one or more prompts on the object.
2. Press ++enter++ to run the model on the placed prompts.
3. If the mask grabbed too much, add a **negative** prompt and run again.
4. Accept the result, then assign a label with ++l++.

<figure class="iq-media">
  <video poster="../../assets/media/prompt-vocabulary.png" autoplay muted loop playsinline preload="none">
    <source src="../../assets/media/prompt-vocabulary.webm" type="video/webm">
    <source src="../../assets/media/prompt-vocabulary.mp4" type="video/mp4">
  </video>
  <figcaption>Positive point → negative point corrects an over-segment → box → polygon → freehand.</figcaption>
</figure>

## Controlling what a prompt does

++a++ cycles the **prompt action**:

| Setting | Behaviour |
|---|---|
| **Nothing** | Prompts stay on the canvas until you run or add them. |
| **Run AI** | Every prompt runs the model as soon as it is placed. |
| **Add** | A polygon or freehand outline becomes an object as soon as you close it. Points and boxes are not offered. |

*Nothing* is the right default when you are placing several prompts for one
object. *Run AI* is faster when each prompt is its own object.

## The other two runs

Beyond prompted segmentation (++1++), the workspace offers:

- ++2++ — **Suggest similar instances**: propagate from what you have already
  annotated to visually similar objects in the image.
- ++3++ — **Instance segmentation**: run an instance model over the image rather
  than a single prompt.

<div class="iq-shot-todo">
  <span><strong>Recording slot — <code>suggest-similar</code></strong><br>
  Annotate one object, then propagate to similar instances across the image.<br>
  8–12 s · dark theme · 1280×800</span>
</div>

## Working at speed

- ++left++ / ++right++ move between images; the filmstrip shows where you are.
- ++space++ held pans; ++0++ fits to screen; ++t++ cycles label chips on and off.
- ++cmd+z++ undoes the last prompt first, and only then your annotation history.
- ++question++ opens the [full shortcut sheet](../reference/shortcuts.md).

**Next:** [Draw and refine manually](draw-and-refine.md)
