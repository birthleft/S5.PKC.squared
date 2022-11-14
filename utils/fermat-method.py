import math
from typing import Union


def fermat_method(n: int, b: int) -> Union[bool, str]:
    t0 = math.isqrt(n)  # https://docs.python.org/3.8/library/math.html#math.isqrt

    for t in range(t0 + 1, t0 + b + 1):
        t2n = t ** 2 - n
        s_float = math.sqrt(t2n)
        s = int(s_float)
        print(f"t^2 - n = {t2n}, perfect square (yes/no) = {'yes' if s_float == s else 'no'}")
        # print(f"t = {t}, s = {s}, s_float = {s_float}")
        if s_float == s:
            print(f"s = {s}, t = {t}")
            return f"{t - s} * {t + s}"

    return False


if __name__ == '__main__':
    print(fermat_method(9699, 20))
