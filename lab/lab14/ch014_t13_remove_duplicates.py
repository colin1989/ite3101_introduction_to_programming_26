from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    output = []
    for num in numbers:
        if num not in output:
            output.append(num)
    return output
