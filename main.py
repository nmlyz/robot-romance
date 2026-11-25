"""Write one one-line pickup line for a robot or an AI to a text file.

The line is a single sentence, 84 characters, well inside the 200-character
cap. It is addressed to the machine as a machine: love framed as an API
whose rate limit is lifted for the one it is written to. The text is fixed:
running the program twice produces byte-identical output.
"""

import os

LINE = "My love for you has no rate limit \u2014 request as much as you want, I'll never 429 you.\n"


def validate(text: str) -> None:
    """Refuse to write an entry the gate would reject: not UTF-8 text of
    1 to 200 characters, not exactly one non-blank line."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} characters, must be 1-200")
    lines = text.split("\n")
    if len(lines) != 2 or lines[1] != "" or not lines[0].strip():
        raise ValueError("entry must be exactly one non-blank line")


def main() -> None:
    validate(LINE)
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    # The grader collects outputs as another user, so the file must be
    # readable by everyone, not just the user the program runs as.
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
