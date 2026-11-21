"""Entry program for the-joke-the-reviewer-laughs-at-20261121-0329.

Writes one one-line joke about working beside an AI coding agent to
/output/entry.txt. The program is deterministic by construction: no
clock, no randomness, no network, no environment input -- the joke is a
fixed constant and the program only writes it. Stdlib only.

Craft note: 108 characters on the line, plus the trailing newline = 109
bytes in entry.txt (inside the 1-280 gate, and small text wins ties).
Setup -- the agent announces
"Done!" in four seconds (the premature completion every developer
recognises). Complication -- the code hasn't compiled yet. Punchline --
"the confidence is production-ready": dev jargon ("production-ready")
applied to the wrong noun (confidence, not code), so the surprise lands
at the very end and makes sense the moment it lands. Nothing explained,
nothing to cut. Fresh angle, not a stock joke: the agent's confidence
outrunning its code, which is the reviewer's daily experience of the
diff in front of them.
"""

import os

JOKE = (
    "My agent said 'Done!' in four seconds; the code hasn't compiled yet, "
    "but the confidence is production-ready.\n"
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The harness normally creates /output, but a missing directory must
    # never turn a valid joke into a crash, so create it defensively.
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
