from typing import List

def purify(numbers: List[int]) -> List[int]:
    purified = []
    for num in numbers:
        if num % 2 == 0:
            purified.append(num)
    return purified