"""Funniest Autocorrect Fail — entry program.

SPDX-License-Identifier: MIT

Writes the entry text to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
No network, no randomness, no arguments: the entry is fixed.

The entry is a 153-character autocorrect fail: a text about bringing
donuts became a promise to bring donkeys, and now four donkeys are in
the parking lot while HR wants a word. The slip is clear, the wrong word
is a surprise, and the joke lands on first read — no explanation needed.
"""

import os

ENTRY = 'Texted my boss I would bring the donuts — autocorrect sent I would bring the donkeys. There are now four donkeys in the parking lot, and HR wants a word.'
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")
MAX_CHARS = 199  # bounty character limit; ENTRY must fit within it.


def main() -> None:
    # Validate before writing: the entry must be non-empty and within limit.
    assert ENTRY, "entry must not be empty"
    assert len(ENTRY) <= MAX_CHARS, f"entry is {len(ENTRY)} chars, limit is {MAX_CHARS}"
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Write the entry verbatim, exactly as defined above — no trailing newline,
    # so the file holds precisely the failed text the judge will read.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
