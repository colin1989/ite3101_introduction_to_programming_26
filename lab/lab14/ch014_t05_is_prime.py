def is_prime(x: int) -> bool:
    for n in range(2, x - 1):
        print("x : %s n : %s" % (x, n))
        if x / n == 0:
            return False
    return True


print(is_prime(1))
print(is_prime(2))
print(is_prime(3))
print(is_prime(4))
print(is_prime(4))
