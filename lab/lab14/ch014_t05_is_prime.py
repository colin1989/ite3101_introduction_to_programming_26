def is_prime(x: int) -> bool:
    if x == 2:
        return True
    for n in range(2, x - 1):
        print("x : %s n : %s" % (x, n))
        if x / n == 0:
            return False
        return True

is_prime(1)
is_prime(2)
is_prime(3)