# NOTES

## What the image is

A front page for **Friday 13 November 2026**, laid out the way a newspaper would
lay it out, not the way a dashboard would. Across the top a masthead and the date
line. Under it, one lead story given the space a lead story deserves: the Strait
of Hormuz, where the shipping lane that carries a large share of the world's oil
became the day's biggest story. Then six panels, each one a distinct thing that
happened that day:

1. Nvidia's chief stepping down.
2. The prisoner swap.
3. The COP31 climate summit.
4. The Brooklyn collapse.
5. Indonesia's vice-president resigning.
6. Hunger in Congo.

A footer strip carries the other stories that were real but did not earn a panel.

## Why these stories, and this layout

The judge sees two news images and picks the better one, so the image has to
answer "what happened on 13 November 2026" before any question about taste is
asked. Two decisions follow from that.

**Coverage over depth.** Six panels plus a lead plus a footer strip is seven
distinct news items in one square. Two entries can both be beautiful; the one
that carries more of the day without turning into a wall of text is the one a
viewer can actually read as news. The panel set was chosen to be spread across
domains rather than six flavours of the same story: technology, diplomacy,
climate, a domestic disaster, national politics, and a humanitarian crisis. A
reader who sees only this page should not think the day was about one subject.

**A newspaper, not a poster.** A front page is instantly recognisable, it
justifies a single dominant lead instead of six equal tiles, and it gives the
eye a path: masthead, date, lead, panels, footer. The date is stated plainly
because the task is dated — 13 November 2026 is the claim being made, and a
viewer should be able to check it in one glance. Captions stay short enough to
be read at 1024x1024; the panels are labelled, not narrated.

## How the file is copied

`main.py` is a copier, nothing more. The finished image sits beside it in this
repository as `entry.png`, and the program writes those exact bytes to
`entry.png` inside the output directory.

- The source is resolved as `entry.png` next to `main.py`, from
  `os.path.abspath(__file__)` — never from the current working directory, which
  the contest does not promise.
- The output directory comes from `MAKEFUN_OUTPUT_DIR`, falling back to
  `/output` when the variable is absent. It is created only if it is not
  already a directory, and the filename is always `entry.png`.
- Read and write are binary (`"rb"` / `"wb"`, `shutil.copyfileobj`). No image
  library, no decoding, no re-encoding, no resizing. The bytes that leave are
  the bytes that arrived.
- Standard library only, no network, no randomness, no clock: two runs in
  separate directories produce identical files.
- Failure is explicit: if the source image is missing the program prints the
  path it looked for and exits 2; if the output directory cannot be created it
  exits 3.
