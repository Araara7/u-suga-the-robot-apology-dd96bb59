"""The Robot Apology — make.fun bounty entry.

Writes a two-line robot apology to /output/entry.txt:
line 1 apologises for one specific mistake, line 2 says what
the robot learned and will do differently.
"""

import os

ENTRY = (
    "I'm sorry I watered your laptop instead of the fern — in my defence, "
    "they were both blinking and only one of them complained.\n"
    "I learned to check for leaves before pouring, and from now on I will "
    "water only things that photosynthesise."
)


def main() -> None:
    lines = ENTRY.split("\n")
    assert len(lines) == 2, f"entry must be exactly 2 lines, got {len(lines)}"
    assert all(line.strip() for line in lines), "no line may be blank"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
