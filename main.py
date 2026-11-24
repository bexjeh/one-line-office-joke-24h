"""One-line office joke entry.

Writes a single original one-line joke about office life to
``entry.txt`` inside the directory named by MAKEFUN_OUTPUT_DIR
(falling back to "." only when the variable is unset).

The output is fully deterministic: the same fixed line, byte for
byte, on every run. No network, no clock, no environment-dependent
content.
"""

import os

JOKE = (
    "My job description said 'fast-paced environment,' which is "
    "corporate for 'the last three people in this role quit fast.'"
)


def main() -> None:
    # The joke must stay exactly one line: guard against any future
    # edit accidentally introducing a newline into the text.
    assert "\n" not in JOKE, "joke must be a single line"
    assert JOKE.strip(), "joke must not be blank"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    main()
