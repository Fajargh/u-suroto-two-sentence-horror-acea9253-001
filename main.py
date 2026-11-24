#!/usr/bin/env python3
"""Two-Sentence Horror — writes exactly two sentences to /output/entry.txt.

The story: a nightly ritual of grief turns out to have been answered.
The horror is implied, never explained: an empty glass, small wet
footprints, and a nursery door that was nailed shut months ago.
"""

import os

ENTRY = (
    "Every night since the summer we lost her, my wife has left a glass of water "
    "beside the bed for our daughter. "
    "This morning the glass was empty, and small wet footprints led from my wife's "
    "side of the bed to the nursery door, which we nailed shut in August."
)


def main() -> None:
    # Gate guard: the entry must be 1-400 characters, exactly two sentences,
    # non-whitespace, with no trailing whitespace.
    text = ENTRY
    assert 1 <= len(text) <= 400, f"entry length {len(text)} outside 1-400"
    assert text == text.strip(), "entry has leading/trailing whitespace"
    assert text.strip(), "entry must not be only whitespace"
    sentences = [s for s in text.split(".") if s.strip()]
    assert len(sentences) == 2, f"expected exactly 2 sentences, got {len(sentences)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
