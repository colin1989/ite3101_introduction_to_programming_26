from typing import List


def production(integers: List[int]) -> List[int]:
    output = 1
    for num in integers:
        output *= num
    return output
