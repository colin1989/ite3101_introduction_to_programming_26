from typing import List

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]


def grades_sum(grades_input: List[float]) -> float:
    total = 0
    for g in grades_input:
        total += g
    return total

print(grades_sum(grades))