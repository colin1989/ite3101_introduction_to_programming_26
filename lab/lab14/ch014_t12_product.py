from typing import List


def product(integers: List[int]) -> List[int]:
    output = 1
    for num in integers:
        output *= num
    return output
