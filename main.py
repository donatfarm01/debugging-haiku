#!/usr/bin/env python3
"""Write one debugging haiku to /output/entry.txt.

The haiku is a fixed constant: three lines, 5-7-5 syllables, well under
200 characters. The program is fully deterministic -- every run writes
the exact same bytes.
"""

import os

HAIKU = """Still the breakpoint waits
while the log insists it works
and I wrote the bug
"""
# Syllables per line: 5, then 7, then 5 -- seventeen in all.
# Line one pictures the breakpoint waiting; line two, the log that claims
# all is well; line three turns the poem back on its author.


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
