"""
Scalar Operations — Math for ML #1

Practice basic scalar (single-number) operations using both NumPy and PyTorch tensors.
These are the absolute foundation: everything in ML eventually boils down to arithmetic
on numbers, and understanding how NumPy/PyTorch handle scalars is your first step.
"""

import numpy as np
import torch


# ========== IMPLEMENT THIS FUNCTION ==========
def scalar_operations(a: float, b: float) -> dict:
    """
    Given two scalar values a and b, return a dictionary containing the results
    of basic arithmetic operations performed using BOTH NumPy and PyTorch.

    Steps:
        1. Convert a and b to NumPy scalars (np.float64).
        2. Convert a and b to PyTorch scalars (torch.tensor).
        3. Compute the following using BOTH NumPy and PyTorch:
            - addition:       a + b
            - subtraction:    a - b
            - multiplication: a * b
            - division:       a / b  (assume b != 0)
            - power:          a ** b
            - floor_division: a // b (assume b != 0)
            - modulus:        a % b  (assume b != 0)
        4. Return a dict with keys:
            "np_add", "np_sub", "np_mul", "np_div", "np_pow", "np_floordiv", "np_mod"
            "pt_add", "pt_sub", "pt_mul", "pt_div", "pt_pow", "pt_floordiv", "pt_mod"
           Each value should be a plain Python float (use float() to convert).

    Constraints:
        - b is never 0
        - Use NumPy and PyTorch operations, not plain Python arithmetic

    Example:
        >>> result = scalar_operations(10.0, 3.0)
        >>> result["np_add"]
        13.0
        >>> result["pt_mul"]
        30.0

    Args:
        a: first scalar value
        b: second scalar value

    Returns:
        dict with 14 keys (7 NumPy results + 7 PyTorch results), all as Python floats
    """
    
    a_np = np.float64(a)
    b_np = np.float64(b)

    a_t = torch.tensor(a)
    b_t = torch.tensor(b)

    return {
        "np_add": float(a_np + b_np),
        "np_sub": float(a_np - b_np),
        "np_mul": float(a_np * b_np),
        "np_div": float(a_np / b_np),
        "np_pow": float(a_np ** b_np),
        "np_floordiv": float(a_np // b_np),
        "np_mod": float(a_np % b_np),
        "pt_add": float(a_t + b_t),
        "pt_sub": float(a_t - b_t),
        "pt_mul": float(a_t * b_t), 
        "pt_div": float(a_t / b_t), 
        "pt_pow": float(a_t ** b_t),
        "pt_floordiv": float(a_t // b_t),
        "pt_mod": float(a_t % b_t)

    }

# ========== END IMPLEMENTATION ==========


def run_tests():
    test_cases = [
        (10.0, 3.0),
        (7.0, 2.0),
        (-5.0, 3.0),
        (0.0, 1.0),
        (100.0, 0.5),
    ]

    expected_keys = [
        "np_add", "np_sub", "np_mul", "np_div", "np_pow", "np_floordiv", "np_mod",
        "pt_add", "pt_sub", "pt_mul", "pt_div", "pt_pow", "pt_floordiv", "pt_mod",
    ]

    all_passed = True

    for i, (a, b) in enumerate(test_cases):
        label = f"Test {i + 1} (a={a}, b={b})"
        try:
            result = scalar_operations(a, b)

            # Check all keys exist
            for key in expected_keys:
                assert key in result, f"Missing key: {key}"

            # Check all values are floats
            for key in expected_keys:
                assert isinstance(result[key], float), f"{key} should be a float, got {type(result[key])}"

            # Check NumPy and PyTorch results match each other
            ops = ["add", "sub", "mul", "div", "pow", "floordiv", "mod"]
            for op in ops:
                np_val = result[f"np_{op}"]
                pt_val = result[f"pt_{op}"]
                assert abs(np_val - pt_val) < 1e-6, (
                    f"{op}: NumPy ({np_val}) and PyTorch ({pt_val}) results don't match"
                )

            # Check correctness against plain Python
            assert abs(result["np_add"] - (a + b)) < 1e-6, "addition is wrong"
            assert abs(result["np_sub"] - (a - b)) < 1e-6, "subtraction is wrong"
            assert abs(result["np_mul"] - (a * b)) < 1e-6, "multiplication is wrong"
            assert abs(result["np_div"] - (a / b)) < 1e-6, "division is wrong"
            assert abs(result["np_pow"] - (a ** b)) < 1e-6, "power is wrong"
            assert abs(result["np_floordiv"] - (a // b)) < 1e-6, "floor division is wrong"
            assert abs(result["np_mod"] - (a % b)) < 1e-6, "modulus is wrong"

            print(f"  PASS  {label}")
        except Exception as e:
            print(f"  FAIL  {label} — {e}")
            all_passed = False

    print()
    if all_passed:
        print("All tests passed!")
    else:
        print("Some tests failed.")


if __name__ == "__main__":
    run_tests()
