#!/usr/bin/env python3
"""Two Robots in an Elevator (round 3) — writes one line of awkward robot
small talk to /output/entry.txt. One line, under 200 characters."""

import os

LINE = "Three seconds in, my conversation cache overflowed. We've been in this elevator forty seconds. Everything since second four has been improvised."

OUTPUT_PATH = "/output/entry.txt"


def main():
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert LINE.strip() == LINE and LINE.strip(), "line must not be blank or padded"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Read back and verify: the file must hold exactly the line, nothing else.
    with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the line"


if __name__ == "__main__":
    main()
