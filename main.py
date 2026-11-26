#!/usr/bin/env python3
"""The Dog Reviews the Mailman — entry writer.

Writes one funny one-line review, in a dog's voice, to /output/entry.txt.

The review itself is a fixed, hand-written string: the program's only job
is to emit it exactly, with no trailing newline, and to sanity-check the
gate (1-200 characters, a single line, not whitespace-only) before writing,
so a bad string can never be submitted by accident.
"""

import os
import sys

REVIEW = (
    "He comes every day, never once throws the letters, and still expects "
    "a wag. Worst fetch partner I have ever met \u2014 and I wait at the "
    "gate for him anyway."
)

OUTPUT_PATH = "/output/entry.txt"


def check_gate(text):
    """Return an error string if the text fails the competition gate."""
    if not text:
        return "entry is empty"
    if len(text) > 200:
        return "entry is %d characters, over the 200 limit" % len(text)
    if text.strip() == "":
        return "entry is whitespace-only"
    if "\n" in text or "\r" in text:
        return "entry is not a single line"
    return None


def main():
    error = check_gate(REVIEW)
    if error:
        print("gate check failed: %s" % error, file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(REVIEW)

    # Verify what landed on disk matches the review exactly, so a
    # half-written or re-encoded file is caught here, not by the gate.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != REVIEW:
        print("verification failed: file does not match the review",
              file=sys.stderr)
        return 1

    print("wrote %d characters to %s" % (len(REVIEW), OUTPUT_PATH))
    return 0


if __name__ == "__main__":
    sys.exit(main())
