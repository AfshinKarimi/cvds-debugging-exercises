from typing import List
def id_to_fruit(fruit_id: int, fruits: List[str]) -> str:
    if fruit_id < 0 or fruit_id >= len(fruits):
        raise IndexError(
            f"Fruit id {fruit_id} is out of range for list length {len(fruits)}."
        )
    return fruits[fruit_id]
