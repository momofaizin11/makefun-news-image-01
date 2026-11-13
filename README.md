# news-image-01 — 13 November 2026 in one image

A front page for Friday 13 November 2026: a masthead and date line, a lead story
on the Strait of Hormuz, six panels covering Nvidia's chief stepping down, the
prisoner swap, the COP31 climate summit, the Brooklyn collapse, Indonesia's
vice-president resigning and hunger in Congo, and a footer strip of the day's
other stories. `entry.png` (1024x1024, RGB, PNG) is the finished image and the
whole entry; `main.py` does not draw it, it copies it byte for byte into the
output directory, reading `MAKEFUN_OUTPUT_DIR` (default `/output`) and writing
`entry.png` there. It is standard library only, deterministic and has no
network, clock or randomness. See `NOTES.md` for the reasoning behind the image.

Run it:

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```
