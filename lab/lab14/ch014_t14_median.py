import math
from typing import List


def median(numbers: List[int]) -> List[int]:
    numbers = sorted(numbers)
    len_numbers = len(numbers)
    if len_numbers == 1:
        return numbers[0]
    before_median = numbers[math.floor(len_numbers/2)-1]
    after_median = numbers[math.ceil(len_numbers/2)]

    return (before_median + after_median) / 2
