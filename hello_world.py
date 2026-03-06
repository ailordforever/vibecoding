def hello_world() -> str:
    """
    Return the string "Hello, World!".

    - Takes no arguments.
    - Returns exactly the string: Hello, World!
    - Must match capitalization, spacing, and punctuation exactly.

    Example:
        >>> hello_world()
        'Hello, World!'
    """
    # ========== IMPLEMENT THIS FUNCTION ==========
    return "Hello, World!"
    # ========== END IMPLEMENTATION ==========


def main() -> None:
    tests = [
        ("basic return value", "Hello, World!"),
        ("exact string match", "Hello, World!"),
        ("is a string", str),
        ("not empty", True),
        ("correct length", 13),
    ]

    results = []

    # Test 1 — returns the correct value
    try:
        result = hello_world()
        assert result == tests[0][1], f"Expected 'Hello, World!', got {result!r}"
        print("Test 1 (basic return value)       : PASS")
        results.append(True)
    except Exception as e:
        print(f"Test 1 (basic return value)       : FAIL — {e}")
        results.append(False)

    # Test 2 — exact string (redundant on purpose, catches mutation)
    try:
        result = hello_world()
        assert result == tests[1][1], f"Expected 'Hello, World!', got {result!r}"
        print("Test 2 (exact string match)       : PASS")
        results.append(True)
    except Exception as e:
        print(f"Test 2 (exact string match)       : FAIL — {e}")
        results.append(False)

    # Test 3 — return type is str
    try:
        result = hello_world()
        assert isinstance(result, str), f"Expected str, got {type(result).__name__}"
        print("Test 3 (is a string)              : PASS")
        results.append(True)
    except Exception as e:
        print(f"Test 3 (is a string)              : FAIL — {e}")
        results.append(False)

    # Test 4 — not empty or None
    try:
        result = hello_world()
        assert result, "Returned empty or None"
        print("Test 4 (not empty)                : PASS")
        results.append(True)
    except Exception as e:
        print(f"Test 4 (not empty)                : FAIL — {e}")
        results.append(False)

    # Test 5 — correct length
    try:
        result = hello_world()
        assert len(result) == tests[4][1], f"Expected length 13, got {len(result)}"
        print("Test 5 (correct length)           : PASS")
        results.append(True)
    except Exception as e:
        print(f"Test 5 (correct length)           : FAIL — {e}")
        results.append(False)

    print(f"\n{sum(results)}/{len(results)} tests passed.")


if __name__ == "__main__":
    main()
