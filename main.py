#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off — a make.fun bounty entry.

The out-of-office reply has a better work-life balance than its
owner does: it leaves at five, never answers on weekends, and nobody
ever asks it to stay late for a quick sync. The joke lands because
the auto-reply is the only one in the office with boundaries — and
it got them by being a template nobody can guilt-trip.

One line, written to the file the harness reads. Nothing else happens.
"""

from os import environ, makedirs, path

# The entry itself. One line about office life: the auto-reply with
# a healthier relationship to work than the human who wrote it.
# The reply is the only one in the office with boundaries.
LINE = "My out-of-office reply has a better work-life balance than I do."

# The bounty gate for this entry allows at most 199 characters.
LIMIT = 199


def entry_text():
    """Return the entry line, checked against the bounty gate."""
    text = LINE
    if not 1 <= len(text) <= LIMIT:
        raise ValueError(f"entry is {len(text)} chars, gate allows 1-{LIMIT}")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    """Write the entry line to the harness output file."""
    out_dir = environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    makedirs(out_dir, exist_ok=True)
    target = path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(entry_text())


if __name__ == "__main__":
    main()
