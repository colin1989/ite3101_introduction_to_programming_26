from typing import List


def median(numbers: List[int]) -> List[int]:
    numbers = sorted(numbers)
    len_numbers = len(numbers)
    # before_median = numbers[:len_numbers // 2]
    # after_median = numbers[len_numbers // 2 + (len_numbers % 2):

