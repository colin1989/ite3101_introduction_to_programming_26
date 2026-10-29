import math
from typing import List


def median(numbers: List[int]) -> List[int]:
    numbers = sorted(numbers)
    len_numbers = len(numbers)
    before_median = numbers[math.ceil(len_numbers/2)-1]
    after_median = numbers[math.ceil(len_numbers/2)-1]

