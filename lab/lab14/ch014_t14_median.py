import math
from typing import List


def median(numbers: List[int]) -> float:
    numbers = sorted(numbers)
    mid_index = len(numbers) // 2
    if len_numbers % 2 != 0:
        return numbers[math.floor(len_numbers/2)]
    else:
        before_median = numbers[math.floor(len_numbers/2)-1]
        after_median = numbers[math.ceil(len_numbers/2)]

    return (before_median + after_median) / 2
