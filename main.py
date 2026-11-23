#!/usr/bin/env python3
"""Dad Joke Showdown: one dad joke, 200 characters or fewer.

Writes the joke to /output/entry.txt.
Deterministic: the same joke every run, no input, no network.
"""

import os

JOKE = (
    "I asked my son what he wanted for dinner. "
    "He said, 'Whatever you make, Dad.' So I made reservations."
)


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke is {len(text)} characters, must be 1-200"
    assert text.strip(), "joke must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to /output/entry.txt")


if __name__ == "__main__":
    main()
