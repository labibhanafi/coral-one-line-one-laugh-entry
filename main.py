"""One Line, One Laugh — entry writer.

Writes a single original one-liner to /output/entry.txt.
Deterministic: the same bytes on every run.
"""

import os

ENTRY = "My smartwatch buzzed to remind me to breathe, so I held my breath to see if it would panic — it called my emergency contact."

# Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"


def main():
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the file is exactly the one line.
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
