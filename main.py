#!/usr/bin/env python3
"""Write the competition artifact: one office joke, at most 200 characters.

The joke lives in entry.txt beside this file (single source of truth). The
same text is embedded below so the program still emits correct bytes if it is
run without its repository tree. Output is byte-identical on every run.
"""

import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.txt")

# Fallback copy of entry.txt, kept in sync with it.
JOKE = (
    'Our all-hands opened with "there are no bad questions." I asked one. '
    'The Q&A doc went read-only mid-question, and HR has booked me a '
    '15-minute "quick chat."'
)

MAX_CHARS = 200


def load_joke():
    """Return the joke collapsed to one line with no surrounding whitespace."""
    text = JOKE
    if os.path.isfile(SOURCE):
        with open(SOURCE, encoding="utf-8") as handle:
            text = handle.read()
    return " ".join(text.split())


def main():
    joke = load_joke()
    if not joke or len(joke) > MAX_CHARS:
        print("entry fails the gate: %d characters" % len(joke), file=sys.stderr)
        return 1

    target = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(target, exist_ok=True)
    path = os.path.join(target, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(joke)

    print("wrote %s (%d characters)" % (path, len(joke)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
