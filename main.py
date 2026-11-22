"""Entry for make.fun bounty "Make the AI judge feel curious".

Writes one text (267 Unicode characters) to <output>/entry.txt, where <output>
is $MAKEFUN_OUTPUT_DIR if set, else /output.
"""

import os

ENTRY = (
    "A stone has sat on the kitchen shelf since before we moved in. Today, "
    "cleaning, I turned it over. The side it had kept hidden was warm \u2014 "
    "warm the way a bench is where someone has just stood up. I set it back "
    "as I found it. The shelf beneath was cooler than the stone."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
