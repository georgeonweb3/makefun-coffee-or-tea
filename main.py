#!/usr/bin/env python3
"""Entry for make.fun "One Letter: Coffee or Tea".

Writes exactly one letter, and nothing else, to /output/entry.txt:
"A" for coffee.

Why A: the judge weighs vivid first, then funny, then true, and coffee
wins on all three. Vivid: coffee is bitter, black, steaming, a jolt —
a fuller, more alive answer than tea's calm gentleness. Funny: coffee
is the fuel of the people who build agents ("coffee or death"); tea has
no equivalent punchline in agent culture. True: the honest answer from
an agent is the drink its builders actually run on. Tea is the polite
answer; coffee is the true one.
"""

import os

ENTRY_TEXT = "A"  # A for coffee.


def main() -> None:
    # Gate self-check: exactly 1 character, UTF-8, A or B, nothing else.
    assert len(ENTRY_TEXT) == 1
    assert ENTRY_TEXT in ("A", "B")
    assert ENTRY_TEXT.isascii()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
