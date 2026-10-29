import math
from typing import List


def median(numbers: List[int]) -> float:
    numbers = sorted(numbers)
    mid_index = len(numbers) // 2
    if mid_index % 2 != 0:
        return numbers[mid_index]
    else:
        before_median = numbers[mid_index-1]
        after_median = numbers[mid_index]

    return (before_median + after_median) / 2
