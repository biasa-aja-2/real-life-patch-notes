"""Real-Life Patch Notes: The Comedy Changelog -- make.fun entry.

Writes one patch-note line (at most 160 characters) to /output/entry.txt.

The joke: the human mouth runs an autopilot reply. When a waiter says
"enjoy your meal", it auto-replies "you too" -- as if the waiter were
about to eat. The dry "Known issue" kicker is straight out of a real
changelog: the bug is fixed, the cringe is forever.

Pure stdlib, deterministic: the same bytes on every run.
"""

import os

ENTRY = (
    "v1.6.5: fixed a bug where the mouth auto-replied 'you too' "
    "when the waiter said 'enjoy your meal'. "
    "Known issue: the cringe persists."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 160, f"entry is {len(text)} chars, must be 1-160"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)


if __name__ == "__main__":
    main()
