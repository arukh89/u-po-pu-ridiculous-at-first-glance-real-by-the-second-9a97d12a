"""Ridiculous at First Glance, Real by the Second.

Writes one sentence to /output/entry.txt: a pitch for a startup that
rents out professional emergency contacts. Deterministic, stdlib only.
"""

import os

OUTPUT_PATH = "/output/entry.txt"

ENTRY = (
    "We rent out professional emergency contacts, because hospitals and "
    "landlords demand a name, and solo movers will pay $30 a month for a "
    "stranger who answers the phone."
)

# Self-check the gate before writing: one sentence, 1-200 characters.
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
