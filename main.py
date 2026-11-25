"""One Line, Big Laugh entry.

Writes a single funny line (at most 200 characters) to /output/entry.txt.
Stdlib only, deterministic, no network.

The joke: a smartwatch celebrates 10,000 steps, then undercuts the
celebration — 9,998 of them were just anxious pacing, not exercise.
Specific, relatable, and the twist lands in the final clause.
"""

ENTRY = "My smartwatch congratulated me on 10,000 steps, then quietly noted that 9,998 of them were just me pacing while anxious."


def main():
    assert 1 <= len(ENTRY) <= 200, "ENTRY must be 1-200 characters"
    assert ENTRY.strip(), "ENTRY must not be blank"
    try:
        out_path = "/output/entry.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        out_path = "./output/entry.txt"
        import os

        os.makedirs("./output", exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
    with open(out_path, "r", encoding="utf-8") as f:
        assert f.read() == ENTRY, "read-back mismatch"
    print(ENTRY)
    print(f"Characters: {len(ENTRY)}")


if __name__ == "__main__":
    main()
