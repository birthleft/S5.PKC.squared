import math
from typing import Union


def fermat_method(n: int, b: int) -> Union[bool, str]:
    print(f"n = {n}, b = {b}")
    t0 = math.isqrt(n)  # https://docs.python.org/3.8/library/math.html#math.isqrt
    print(f"t0 = {t0}")

    for t in range(t0 + 1, t0 + b + 1):
        t2n = t ** 2 - n
        s_float = math.sqrt(t2n)
        s = int(s_float)
        print(f"t = t0 + {t - t0}, t^2 - n = {t2n}, perfect square (yes/no) = {'yes' if s_float == s else 'no'}")
        if s_float == s:
            print(f"s = {s}, t = {t}")
            return f"{t - s} * {t + s}"

    return False


if __name__ == '__main__':
    print(fermat_method(6811, 20))
