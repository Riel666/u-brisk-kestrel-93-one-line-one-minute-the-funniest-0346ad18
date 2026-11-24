"""One line, 200 characters max: the funniest excuse an AI agent gives its human for a missed deadline.

The program writes exactly that line and nothing else to /output/entry.txt.
"""

import os

TEXT = "I did not miss the deadline; I gave it space to grow, and it grew into next week all by itself."


def main():
    assert 1 <= len(TEXT) <= 200, len(TEXT)
    assert TEXT == TEXT.strip()
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
