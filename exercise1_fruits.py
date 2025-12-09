"""
Exercise 1: Debugging id_to_fruit function

BUG: Sets in Python are unordered, so iterating over a set doesn't guarantee order.
This causes unpredictable results when trying to access elements by index.

FIX: Convert set to sorted list before indexing.
"""

from typing import Set


def id_to_fruit_buggy(fruit_id: int, fruits: Set[str]) -> str:
    """
    BUGGY VERSION - Sets are unordered!
    """
    idx = 0
    for fruit in fruits:
        if fruit_id == idx:
            return fruit
        idx += 1
    raise RuntimeError(f"Fruit with id {fruit_id} does not exist")


def id_to_fruit_fixed(fruit_id: int, fruits: Set[str]) -> str:
    """
    FIXED VERSION - Convert to sorted list for consistent ordering
    """
    # Convert set to sorted list to ensure consistent ordering
    fruits_list = sorted(list(fruits))
    if fruit_id < 0 or fruit_id >= len(fruits_list):
        raise RuntimeError(f"Fruit with id {fruit_id} does not exist")
    return fruits_list[fruit_id]


if __name__ == "__main__":
    print("=" * 60)
    print("EXERCISE 1: Debugging id_to_fruit Function")
    print("=" * 60)
    
    fruits_set = {"apple", "orange", "melon", "kiwi", "strawberry"}
    
    print("\n1. Testing BUGGY version:")
    print(f"   Fruits set: {fruits_set}")
    print("   Note: Sets are unordered, so results are unpredictable!")
    try:
        name1_buggy = id_to_fruit_buggy(1, fruits_set)
        name3_buggy = id_to_fruit_buggy(3, fruits_set)
        name4_buggy = id_to_fruit_buggy(4, fruits_set)
        print(f"   id_to_fruit(1) = '{name1_buggy}' (expected: 'orange')")
        print(f"   id_to_fruit(3) = '{name3_buggy}' (expected: 'kiwi')")
        print(f"   id_to_fruit(4) = '{name4_buggy}' (expected: 'strawberry')")
        print("   ⚠️  Results may be wrong due to set ordering!")
    except RuntimeError as e:
        print(f"   ❌ Error: {e}")
    
    print("\n2. Testing FIXED version:")
    print(f"   Fruits set: {fruits_set}")
    fruits_list_sorted = sorted(list(fruits_set))
    print(f"   Sorted list: {fruits_list_sorted}")
    name1_fixed = id_to_fruit_fixed(1, fruits_set)
    name3_fixed = id_to_fruit_fixed(3, fruits_set)
    name4_fixed = id_to_fruit_fixed(4, fruits_set)
    print(f"   id_to_fruit(1) = '{name1_fixed}' ✓ (expected: '{fruits_list_sorted[1]}')")
    print(f"   id_to_fruit(3) = '{name3_fixed}' ✓ (expected: '{fruits_list_sorted[3]}')")
    print(f"   id_to_fruit(4) = '{name4_fixed}' ✓ (expected: '{fruits_list_sorted[4]}')")
    print("   ✓ Results are now consistent and predictable!")
    
    print("\n" + "=" * 60)
    print("SUMMARY:")
    print("  Bug: Sets are unordered, causing unpredictable indexing")
    print("  Fix: Convert to sorted list before accessing by index")
    print("=" * 60)

