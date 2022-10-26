import time

from texttable import Texttable

from GCDSolverBinary import BinaryAlgorithm
from GCDSolverEuclidean import EuclideanAlgorithm
from GCDSolverPrimeFactorization import PrimeFactorization
from TestGCD import TestGCD


def test():
    TestGCD().run()


def analysis():
    algorithms = [EuclideanAlgorithm(), BinaryAlgorithm(), PrimeFactorization()]
    inputs = [(3, 4), (10, 5), (3, 12), (4, 12),
              (10, 20), (54, 24), (1234567890, 9876543210),
              (100_000_000_000_000_007, 100_000_000_000_000_009), (100_000_000_000_000_007, 100_000_000_000_000_011),
              (100_000_000_000_000_007, 100_000_000_000_000_007 * 100_000_000_000_000_007)]

    texttable = Texttable()
    texttable.set_cols_width([20, 20, 20, 20])
    texttable.set_cols_align(["c", "c", "c", "c"])
    texttable.add_row(["(a, b)"] + [algorithm.__class__.__name__ for algorithm in algorithms])

    for a, b in inputs:
        row = [f"({a}, {b})"]

        for algorithm in algorithms:
            max_val = 1234567890
            if type(algorithm) == PrimeFactorization and a >= max_val:
                row.append("N/A")
                continue

            start = time.time_ns()
            algorithm.solve(a, b)
            end = time.time_ns()

            row.append(f"{(end - start) / 1000} ms")

        texttable.add_row(row)

    print(texttable.draw())


if __name__ == '__main__':
    test()
    analysis()
