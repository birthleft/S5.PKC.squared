from abc import ABC, abstractmethod


class GCDSolver(ABC):
    @abstractmethod
    def solve(self, a: int, b: int) -> int:
        pass


