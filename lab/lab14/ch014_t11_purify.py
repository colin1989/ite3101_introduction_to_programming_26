from typing import List

def purify(numbers: List[int]) -> List[int]:
    output = []
    for num in numbers:
        if num % 2 == 0:
            output.append(num)
    return output