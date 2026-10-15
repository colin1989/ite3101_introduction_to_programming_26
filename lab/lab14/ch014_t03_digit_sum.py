def digit_sum(n: int) -> int:
    output = 0
    while n > 0:
        out += n%10
        n /= 10
    return output