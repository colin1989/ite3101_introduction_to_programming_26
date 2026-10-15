def digit_sum(n: int) -> int:
    output = 0
    while n > 0:
        output += n%10
        n /= 10
    return output