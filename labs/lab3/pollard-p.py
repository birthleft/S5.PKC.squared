from typing import Callable


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def pollard_p(n: int, x0: int, f: Callable[[int], int] = lambda x: x ** 2 + 1) -> int:
    j = 1
    x_sequence = {0: x0}

    while True:
        x_sequence[j] = f(x_sequence[j - 1]) % n
        j += 1
        x_sequence[j] = f(x_sequence[j - 1]) % n

        # j is even
        d = gcd(abs(x_sequence[j] - x_sequence[j // 2]), n)

        print(f"x{j - 1} = {x_sequence[j - 1]}, x{j} = {x_sequence[j]}, (|x{j} - x{j // 2}|, n) = {d}")

        if 1 < d < n:
            return d

        j += 1


if __name__ == '__main__':
    n = 9983
    x0 = 2
    f1 = pollard_p(n, x0, lambda x: x ** 2 + 1)
    print(f"{n} = {f1} * {n // f1}")
