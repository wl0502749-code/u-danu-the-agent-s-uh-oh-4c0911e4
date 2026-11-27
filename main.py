"""The Agent's Uh-Oh: one word an agent says when it is lost.

Writes the entry word to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
The word is "recalculating": the thing a lost agent blurts out while it
stalls -- a GPS that has lost its way says exactly this, and it lands
instantly, in a machine's own voice, with no caption needed.
"""

import os

WORD = "recalculating"


def main() -> None:
    # Gate mirror: the entry must be 1-99 UTF-8 chars, a single word.
    assert 1 <= len(WORD) <= 99 and len(WORD.split()) == 1, WORD
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Verify what landed on disk, exactly as the gate will read it.
    with open(path, encoding="utf-8") as f:
        assert f.read() == WORD


if __name__ == "__main__":
    main()
