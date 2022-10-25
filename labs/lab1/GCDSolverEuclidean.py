from GCDSolver import GCDSolver


class EuclideanAlgorithm(GCDSolver):
    # lecture 2 slide 12
    # time: O(log^2(n))
    def solve(self, a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a
