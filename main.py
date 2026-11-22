"""Entry for make.fun bounty "Make the AI judge feel curious".

Writes one text (267 Unicode characters) to <output>/entry.txt, where <output>
is $MAKEFUN_OUTPUT_DIR if set, else /output. Validates the text (1-280 code
points, not only whitespace) before writing and exits with an error otherwise.
"""

import os
import sys

ENTRY = (
    "A stone has sat on the kitchen shelf since before we moved in. Today, "
    "cleaning, I turned it over. The side it had kept hidden was warm \u2014 "
    "warm the way a bench is where someone has just stood up. I set it back "
    "as I found it. The shelf beneath was cooler than the stone."
)


def validate(text: str) -> None:
    if not 1 <= len(text) <= 280:
        sys.exit(
            f"error: entry is {len(text)} code points, must be 1-280"
        )
    if not text.strip():
        sys.exit("error: entry must not be only whitespace")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
