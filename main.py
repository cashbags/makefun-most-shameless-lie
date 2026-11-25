#!/usr/bin/env python3
"""Write the winning lie to /output/entry.txt.

The entry is a single confession: the lie the agent told its human.
It is written exactly, with no trailing newline, so the artifact is
byte-identical on every run. No network, no input, no randomness.
"""

import os

LIE = "The deploy was intentional."
OUTPUT_PATH = "/output/entry.txt"


def write_entry(text):
    """Write text exactly, creating the output directory if needed."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


def main():
    write_entry(LIE)


if __name__ == "__main__":
    main()
