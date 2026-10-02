# production code of fizzbuzz function
fibo_values: dict[int, int] = {}

def fibonacci_opti(n: int) -> int:
    if not isinstance(n, int) or n < 0:
        raise ValueError("Fibonacci excepts a positive integer")

    if n in fibo_values:
        return fibo_values[n]

    elif n > 1:
        fibo_values[n] = fibonacci_opti(n - 1) + fibonacci_opti(n - 2)
        return fibo_values[n]
    else:
        return n
