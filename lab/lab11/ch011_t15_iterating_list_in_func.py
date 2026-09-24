from typing import List

n = [3, 5, 7]


def total(numbers: List[int]) -> int:
    result = 0
    for n in numbers:
        result += n

    # for i in range(len(list)):
    #     result += n[i]
    return result
