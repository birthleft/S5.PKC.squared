from GCDSolver import GCDSolver


# https://en.wikipedia.org/wiki/Greatest_common_divisor#Binary_GCD_algorithm
class BinaryAlgorithm(GCDSolver):
    def solve(self, a: int, b: int) -> int:
        d: int = 0

        while a != b:
            if a % 2 == b % 2 == 0:
                a //= 2
                b //= 2
                d += 1
            elif a % 2 == 0:
                a //= 2
            elif b % 2 == 0:
                b //= 2
            elif a > b:
                a = (a - b) // 2
            else:
                b = (b - a) // 2

        return a * 2 ** d
