# About IQUANA

**I**ntelligent **QU**antification, **AN**notation and **A**nalysis.

IQUANA is a research tool built at [DFKI](https://www.dfki.de/) in partnership
with [HIFMB](https://hifmb.de/), for AI-assisted segmentation, annotation and
quantification of scientific image datasets.

## The name

The letters map onto the words like this, and the capitalisation is part of the
name rather than decoration:

| Letters | Word |
|---|---|
| **I** | **I**ntelligent — also read as **I**nteractive or **I**maging |
| **QU** | **QU**antification |
| **AN** | **AN**notation |
| **A** | **A**nalysis |

The **I** is deliberately more than one word. The tool is intelligent in that it
puts models behind the work, interactive in that a human stays in the loop around
every prediction, and about imaging because that is what it measures — and none
of the three is the whole story on its own. The landing page turns the reading
over on purpose.

When writing it out, keep the split as **I** · **QU** · **AN** · **A**. Writing
it as *QUANtification, Annotation* is wrong: it borrows the **AN** from the wrong
word and leaves *annotation* unaccounted for.

## Where it came from

It was built with marine biologists at HIFMB to segment and measure corals and
polyps in reef survey photography — thousands of objects per survey, where
hand-drawing every contour was never going to scale.

The pipeline is general, but it was shaped against a real dataset and a real
measurement question. That is why it insists on things other annotation tools
treat as optional: physical units, provenance, and a review loop around every
model prediction.

## Beyond images

IQUANA is built around image datasets today. The annotation, quantification and
review machinery is not inherently two-dimensional, and we are actively exploring
what it takes to bring the same loop to other scientific modalities.

If you have a dataset that needs annotation and quantification, or you are
interested in a research collaboration, get in touch:
[robert.leist@dfki.de](mailto:robert.leist@dfki.de).

We would rather generalise the tool against a real problem than guess at one.

<div class="iq-cards" markdown>

[**Citing IQUANA**<span>How to reference the tool in a publication.</span>](citation.md)

[**Contributing**<span>Reporting bugs, requesting features, working on the code.</span>](contributing.md)

</div>
