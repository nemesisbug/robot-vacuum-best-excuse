#!/usr/bin/env python3
"""The Robot Vacuum's Best Excuse.

Writes one line -- the funniest excuse a robot vacuum can give for
missing a spot -- to /output/entry.txt.

The line, in the vacuum's own deadpan voice:

    I bumped that crumb twice and it didn't move, so I have officially
    reclassified it as furniture and I don't clean furniture.

Why this line: the judge is a tired homeowner who has heard every
appliance excuse. The joke is rooted in the vacuum's own world (its
bumper sensor doing its job, its map reclassifying what it finds),
it lands on the first read with a clean turn at the end ("I don't
clean furniture"), and it sounds like a small machine keeping a
straight face -- a bureaucratic little robot following protocol,
not an owner apologising for it. Gate: 1-140 characters.
"""

import os

ENTRY = (
    "I bumped that crumb twice and it didn't move, so I have officially "
    "reclassified it as furniture and I don't clean furniture."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, f"entry is {len(text)} chars, gate is 1-140"
    # The file holds the line plus one trailing newline: 125 bytes total,
    # still comfortably inside the 140-character gate.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
