from typing import List

def count(sequence: List[int], item: int) -> int:
    count = 0
    for num in sequence:
        if num == item:
            count += 1
    return count