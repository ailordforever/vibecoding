from typing import List


# ========== IMPLEMENT THIS FUNCTION ==========
def vector_add(a: List[float], b: List[float]) -> List[float]:
    """
    Add two vectors element-wise.

    Given two vectors (lists of numbers) of the same length,
    return a new list where each element is the sum of the
    corresponding elements from a and b.

    Input:
        a: List of floats representing the first vector
        b: List of floats representing the second vector
        (both vectors are guaranteed to have the same length)

    Output:
        A new list representing the element-wise sum of a and b

    Constraints:
        - 0 <= len(a) == len(b) <= 10^5
        - Each element fits in a standard float

    Example:
        vector_add([1, 2, 3], [4, 5, 6]) -> [5, 7, 9]
    """
    return [(x + y) for x,y in zip(a,b)]
# ========== END IMPLEMENTATION ==========


def main() -> None:
    tests = [
        {
            "name": "Basic addition",
            "a": [1, 2, 3],
            "b": [4, 5, 6],
            "expected": [5, 7, 9],
        },
        {
            "name": "Zeros",
            "a": [0, 0, 0],
            "b": [0, 0, 0],
            "expected": [0, 0, 0],
        },
        {
            "name": "Negative numbers",
            "a": [-1, -2, -3],
            "b": [-4, -5, -6],
            "expected": [-5, -7, -9],
        },
        {
            "name": "Mixed positive and negative",
            "a": [10, -20, 30],
            "b": [-10, 20, -30],
            "expected": [0, 0, 0],
        },
        {
            "name": "Empty vectors",
            "a": [],
            "b": [],
            "expected": [],
        },
        {
            "name": "Single element",
            "a": [42.5],
            "b": [7.5],
            "expected": [50.0],
        },
        {
            "name": "Floating point values",
            "a": [1.1, 2.2, 3.3],
            "b": [4.4, 5.5, 6.6],
            "expected": [5.5, 7.7, 9.9],
        },
    ]

    passed = 0
    for t in tests:
        try:
            result = vector_add(t["a"], t["b"])
            # Use approximate comparison for floats
            if result is not None and len(result) == len(t["expected"]):
                ok = all(abs(r - e) < 1e-9 for r, e in zip(result, t["expected"]))
            else:
                ok = False
            assert ok, f"got {result}"
            print(f"  PASS  {t['name']}")
            passed += 1
        except Exception as e:
            print(f"  FAIL  {t['name']} — {e}")

    print(f"\n{passed}/{len(tests)} tests passed.")


if __name__ == "__main__":
    main()
