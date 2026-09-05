Screen recordings land here. See ../../../RECORDING-PLAN.md for the slug list,
lengths and recording conventions.

Naming: <slug>.webm, <slug>.mp4, <slug>.png (poster). All three are produced
from one raw capture by ../../../tools/encode_recording.py -- do not hand-encode
them, or the clips drift apart in size and framing.

    python tools/encode_recording.py "<folder of raw recordings>"

The .md slot markup is written by hand once per slug; see any filled slot for
the shape (figure.iq-media > video[autoplay muted loop playsinline] + poster).
