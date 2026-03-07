import numpy as np
from numpy.typing import NDArray


# ========== IMPLEMENT THIS FUNCTION ==========
def vector_add(a: NDArray[np.float64], b: NDArray[np.float64]) -> NDArray[np.float64]:
    """
    Add two vectors element-wise using NumPy.

    Given two 1-D NumPy arrays of the same length, return a new NumPy array
    where each element is the sum of the corresponding elements from a and b.

    You MUST use NumPy operations — no Python loops or list comprehensions.

    Input:
        a: 1-D numpy array of float64
        b: 1-D numpy array of float64
        (both arrays are guaranteed to have the same shape)

    Output:
        A new 1-D numpy array representing the element-wise sum of a and b

    Constraints:
        - 0 <= len(a) == len(b) <= 10^6
        - Each element fits in float64

    Example:
        vector_add(np.array([1.0, 2.0, 3.0]), np.array([4.0, 5.0, 6.0]))
        -> np.array([5.0, 7.0, 9.0])
    """
    return a + b 
# ========== END IMPLEMENTATION ==========


def main() -> None:
    tests = [
        {
            "name": "Basic addition",
            "a": np.array([1.0, 2.0, 3.0]),
            "b": np.array([4.0, 5.0, 6.0]),
            "expected": np.array([5.0, 7.0, 9.0]),
        },
        {
            "name": "Zeros",
            "a": np.zeros(4),
            "b": np.zeros(4),
            "expected": np.zeros(4),
        },
        {
            "name": "Negative numbers",
            "a": np.array([-1.0, -2.0, -3.0]),
            "b": np.array([-4.0, -5.0, -6.0]),
            "expected": np.array([-5.0, -7.0, -9.0]),
        },
        {
            "name": "Mixed positive and negative",
            "a": np.array([10.0, -20.0, 30.0]),
            "b": np.array([-10.0, 20.0, -30.0]),
            "expected": np.array([0.0, 0.0, 0.0]),
        },
        {
            "name": "Empty arrays",
            "a": np.array([], dtype=np.float64),
            "b": np.array([], dtype=np.float64),
            "expected": np.array([], dtype=np.float64),
        },
        {
            "name": "Single element",
            "a": np.array([42.5]),
            "b": np.array([7.5]),
            "expected": np.array([50.0]),
        },
        {
            "name": "Large arrays",
            "a": np.ones(10000),
            "b": np.full(10000, 2.0),
            "expected": np.full(10000, 3.0),
        },
    ]

    passed = 0
    for t in tests:
        try:
            result = vector_add(t["a"], t["b"])
            assert result is not None, "returned None"
            assert isinstance(result, np.ndarray), f"expected ndarray, got {type(result).__name__}"
            assert result.shape == t["expected"].shape, f"shape {result.shape} != {t['expected'].shape}"
            assert np.allclose(result, t["expected"]), f"got {result}"
            print(f"  PASS  {t['name']}")
            passed += 1
        except Exception as e:
            print(f"  FAIL  {t['name']} — {e}")

    print(f"\n{passed}/{len(tests)} tests passed.")


if __name__ == "__main__":
    main()
