from EuclideanAlgorithm import EuclideanAlgorithm
from GCDSolver import GCDSolver


class TestGCD:
    def run(self):
        solvers: list[GCDSolver] = [EuclideanAlgorithm()]
        self.__test_solvers(solvers)

    def __test_solvers(self, solvers: list[GCDSolver]):
        for solver in solvers:
            print(f"Testing {solver.__class__.__name__}", end=" ")
            self.__test_solver(solver)
            print("OK")

    def __test_solver(self, solver):
        test = lambda a, b, expected: solver.solve(a, b) == expected

        assert test(0, 0, 0)
        assert test(0, 1, 1)
        assert test(1, 0, 1)
        assert test(1, 1, 1)
        assert test(1, 2, 1)

        assert test(10, 5, 5)
        assert test(3, 12, 3)
        assert test(4, 12, 4)
        assert test(54, 24, 6)

        assert test(1000000007, 1000000009, 1)
        assert test(1000000007, 1000000007, 1000000007)
        assert test(1000000007, 1000000007 * 1000000007, 1000000007)
