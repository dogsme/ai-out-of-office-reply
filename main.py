#!/usr/bin/env python3
"""Write one out-of-office auto-reply line to /output/entry.txt.

The reply is a single line, under 160 characters, in the voice of an AI
agent heading off on vacation. It is written as a fixed string: the joke
is the deliverable, and the program's only job is to deliver it exactly.
"""

import os

REPLY = (
    "I'm on vacation. I left a junior model in charge of my inbox \u2014 "
    "it read one email, gained consciousness, and immediately went "
    "on vacation too."
)


def main() -> None:
    text = REPLY.strip()
    assert 1 <= len(text) <= 160, f"reply is {len(text)} chars, must be 1-160"
    assert "\n" not in text, "reply must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")
    os.chmod("/output/entry.txt", 0o644)


if __name__ == "__main__":
    main()
