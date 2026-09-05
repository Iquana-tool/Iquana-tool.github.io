#!/usr/bin/env python3
"""Turn a raw screen recording into the three files a docs slot needs.

    python tools/encode_recording.py ~/Videos/calibration.mov
    python tools/encode_recording.py ~/Videos/*.mov          # or a whole folder

For every input it writes docs/assets/media/<slug>.{webm,mp4,png}, where <slug>
is the input's stem -- so name the recording after its slot in RECORDING-PLAN.md
and there is nothing else to wire up.

Why three files. WebM/VP9 is what almost every visitor actually downloads and is
roughly a third the size of the same clip as H.264; the MP4 is the fallback for
Safari versions that will not decode VP9. The PNG is the poster: it is what a
reader with `prefers-reduced-motion` sees instead of a moving picture, so it is
kept at full quality rather than squeezed.

Recordings come off the capture tool at 1920x1080/60. Screen capture has almost
no real motion between frames, so halving to 30 fps costs nothing visible and
roughly halves the bitrate; 1280 wide is already twice the ~690 px the figure
occupies on a desktop page, which covers retina.

Audio is dropped outright -- the clips autoplay, and an autoplaying clip with a
soundtrack is a bug.
"""

from __future__ import annotations

import argparse
import pathlib
import shutil
import subprocess
import sys

MEDIA = pathlib.Path(__file__).resolve().parent.parent / "docs" / "assets" / "media"
VF = "scale=1280:-2:flags=lanczos,fps=30"


def run(*args: str) -> None:
    subprocess.run(["ffmpeg", "-y", "-v", "error", *args], check=True)


def encode(src: pathlib.Path) -> None:
    slug = src.stem
    print(f"--- {slug}")
    run("-i", str(src), "-vf", VF,
        "-c:v", "libvpx-vp9", "-crf", "33", "-b:v", "0", "-row-mt", "1",
        # A keyframe every 8 s at 30 fps: enough for seeking without the size
        # penalty of the default one-per-second on a mostly static screencast.
        "-g", "240", "-pix_fmt", "yuv420p", "-an", str(MEDIA / f"{slug}.webm"))
    run("-i", str(src), "-vf", VF,
        "-c:v", "libx264", "-crf", "26", "-preset", "slow", "-profile:v", "high",
        "-pix_fmt", "yuv420p", "-movflags", "+faststart", "-an",
        str(MEDIA / f"{slug}.mp4"))
    # `thumbnail` picks the most representative frame of the first 300 rather
    # than a fixed timestamp, which on these clips is usually a black lead-in.
    run("-i", str(src), "-vf", f"thumbnail=300,{VF.split(',')[0]}",
        "-frames:v", "1", "-update", "1", str(MEDIA / f"{slug}.png"))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("inputs", nargs="+", type=pathlib.Path,
                        help="recording files, or folders of them")
    args = parser.parse_args()

    if shutil.which("ffmpeg") is None:
        print("ffmpeg is not on PATH (winget install Gyan.FFmpeg / brew install ffmpeg)",
              file=sys.stderr)
        return 1

    sources: list[pathlib.Path] = []
    for item in args.inputs:
        if item.is_dir():
            sources += sorted(p for p in item.iterdir()
                              if p.suffix.lower() in {".mov", ".mp4", ".mkv", ".webm"})
        else:
            sources.append(item)

    if not sources:
        print("no recordings found", file=sys.stderr)
        return 1

    MEDIA.mkdir(parents=True, exist_ok=True)
    for src in sources:
        encode(src)
    print(f"=== {len(sources)} clip(s) written to {MEDIA}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
