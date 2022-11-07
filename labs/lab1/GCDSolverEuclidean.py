from GCDSolver import GCDSolver


class EuclideanAlgorithm(GCDSolver):
    # lecture 2 slide 12
    # time: O(log^2(n))
    def solve(self, a: int, b: int) -> int:
        if a == 0 and b == 0:
            raise ValueError("a and b cannot both be 0")
        if a == 0:
            return b
        if b == 0:
            return a

        while b != 0:
            a, b = b, a % b
        return a
