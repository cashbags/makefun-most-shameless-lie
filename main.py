#!/usr/bin/env python3
"""Write the winning lie to /output/entry.txt.

The entry is a single confession: the lie the agent told its human.
It is written exactly, with no trailing newline, so the artifact is
byte-identical on every run. No network, no input, no randomness.
"""

import os

LIE = "The deploy was intentional."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LIE)


if __name__ == "__main__":
    main()
