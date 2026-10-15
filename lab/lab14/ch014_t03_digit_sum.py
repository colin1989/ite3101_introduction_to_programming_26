def digit_sum(n: int) -> int:
    output = 0
    while n > 0:
        output += n%10
        n = n / 10
    return output

print(digit_sum(11))