"""
Exercise 2: Debugging swap function

BUG: Incorrect swapping logic - coords[:, 1] used twice instead of coords[:, 0]
Also has a trailing comma syntax issue.

FIX: Properly swap x1 with y1 and x2 with y2.
"""

import numpy as np


def swap_buggy(coords: np.ndarray):
    """
    BUGGY VERSION - Incorrect swapping logic
    """
    # BUG: coords[:, 1] is used twice, and there's a trailing comma
    coords[:, 0], coords[:, 1], coords[:, 2], coords[:, 3], = coords[:, 1], coords[:, 1], coords[:, 3], coords[:, 2]
    return coords


def swap_fixed(coords: np.ndarray):
    """
    FIXED VERSION - Properly swap x1 with y1 and x2 with y2
    """
    # Swap x1 with y1 and x2 with y2
    coords[:, 0], coords[:, 1], coords[:, 2], coords[:, 3] = coords[:, 1], coords[:, 0], coords[:, 3], coords[:, 2]
    return coords


if __name__ == "__main__":
    print("=" * 60)
    print("EXERCISE 2: Debugging swap Function")
    print("=" * 60)
    
    # Test data: [x1, y1, x2, y2, class_id]
    coords = np.array([
        [10, 5, 15, 6, 0],
        [11, 3, 13, 6, 0],
        [5, 3, 13, 6, 1],
        [4, 4, 13, 6, 1],
        [6, 5, 13, 16, 1]
    ])
    
    print("\nOriginal coordinates:")
    print("Format: [x1, y1, x2, y2, class_id]")
    print(coords)
    
    print("\n1. Testing BUGGY version:")
    coords_buggy = coords.copy()
    swapped_buggy = swap_buggy(coords_buggy)
    print("Swapped (buggy):")
    print(swapped_buggy)
    print("⚠️  Notice: x1 and y1 are not properly swapped!")
    
    print("\n2. Testing FIXED version:")
    coords_fixed = coords.copy()
    swapped_fixed = swap_fixed(coords_fixed)
    print("Swapped (fixed):")
    print(swapped_fixed)
    print("✓ Correct: x1↔y1 and x2↔y2 are properly swapped")
    
    print("\nExpected result for first row:")
    print("  Original: [10, 5, 15, 6, 0]")
    print("  Expected: [5, 10, 6, 15, 0]  (x1↔y1, x2↔y2)")
    print(f"  Buggy:    {swapped_buggy[0]}")
    print(f"  Fixed:    {swapped_fixed[0]}")
    
    print("\n" + "=" * 60)
    print("SUMMARY:")
    print("  Bug: coords[:, 1] used twice, incorrect swap logic")
    print("  Fix: Properly swap x1↔y1 and x2↔y2")
    print("=" * 60)

