from GCDSolver import GCDSolver


class PrimeFactorization(GCDSolver):
    def solve(self, a: int, b: int) -> int:
        if a == 0 and b == 0:
            raise ValueError("a and b cannot both be 0")
        if a == 0:
            return b
        if b == 0:
            return a

        gcd = 1
        prime_factorization_of_a = self.prime_factor(a)
        prime_factorization_of_b = self.prime_factor(b)

        for factor in prime_factorization_of_a.keys():
            if factor in prime_factorization_of_b:
                gcd *= factor ** min(prime_factorization_of_a[factor], prime_factorization_of_b[factor])

        return gcd

    @staticmethod
    def prime_factor(number: int) -> dict[int, int]:
        factors = {}
        for i in range(2, number + 1):
            while number % i == 0:
                if i in factors:
                    factors[i] += 1
                else:
                    factors[i] = 1
                number //= i
        return factors

# for i in range(1, 100):
#     print(f"{i}: {PrimeFactorization.prime_factor(i)}")
