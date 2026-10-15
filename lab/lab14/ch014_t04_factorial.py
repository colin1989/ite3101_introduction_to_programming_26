def factorial(x: int) -> int:
    output = 1
    for n range(x):
        output *= n + 1
    return output

print(factorial(2))