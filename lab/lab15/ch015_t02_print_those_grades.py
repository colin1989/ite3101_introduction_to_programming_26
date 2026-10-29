from typing import List

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores: List[int]) -> int:
    sum = 0
    for g in grades:
        sum += g
    return sum
print(grades_sum(grades))