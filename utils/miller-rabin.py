"""
NOTE: it doesn't answer whether the number is prime or not. It just prints the sequence of values that are computed.


Also, the Miller-Rabin test is not a deterministic test. It is a probabilistic test.
"""
import sys
from functools import reduce


# python get bits from int https://stackoverflow.com/questions/9945720/python-extracting-bits-from-a-byte
def is_set(number, n):
    """Return True if the nth bit of number is set."""
    return number & (1 << n) > 0


def repeated_squaring_modular_exponentiation(base, exponent, modulus):
    a: int = 1
    if exponent == 0:
        return a

    c: int = base
    if is_set(exponent, 0):
        a = base

    for i in range(1, exponent.bit_length()):
        c = (c * c) % modulus
        if is_set(exponent, i):
            a = (a * c) % modulus

    return a


def compute_exponent_of_factor(number: int, factor: int):
    exponent = 0
    while number % factor == 0:
        exponent += 1
        number /= 2
    return exponent


def number_as_sum_of_powers_of_2(number: int):
    # return reduce(lambda acc, i: acc + [i] if is_set(n, i) else acc, range(n.bit_length()), [])
    return reduce(lambda x, y: f"{x} + {y}", [f"2^{i}" for i in range(number.bit_length()) if is_set(number, i)])


def compute_and_print_the_relevant_powers_of_2(t, n):
    print(f"t = {bin(t)[2:]} = {number_as_sum_of_powers_of_2(t)}.", end=' ')
    print(f"\n\trelevant exponents: {list([i for i in range(t.bit_length()) if is_set(t, i)])}")
    print()
    for i in range(0, t.bit_length()):
        print(f"2^(2^{i}) mod {n} = {(2 ** 2 ** i) % n}", end=' ')
        print('RELEVANT' if is_set(t, i) else '')
    print()


def miller_rabin(n: int):
    print(f"n = {n}")
    if n <= 1 or n % 2 == 0:
        return False

    # n - 1 = 2^s * t
    s: int = compute_exponent_of_factor(n - 1, 2)
    t: int = (n - 1) >> s  # <=> (n-1)/2^s https://wiki.python.org/moin/BitwiseOperators
    print(f"n - 1 = 2^{s} * {t}")

    compute_and_print_the_relevant_powers_of_2(t, n)

    is_prime = 'TBD'
    for a in [2, 3, 5]:
        sequence = []
        print(f"a = {a}")

        # we need to compute a^t, a^(2t), a^(4t), ..., a^(2^s * t)
        # Step 2 of https://moodle.cs.ubbcluj.ro/pluginfile.php/46227/mod_resource/content/1/pkc-c03.pdf#page=20
        sequence_size = 5  # normally s + 1, but for the quiz it's 5
        for r in range(sequence_size):
            current_sequence_value = repeated_squaring_modular_exponentiation(a, 2 ** r * t, n)

            print(f"{a}^(2^{r} * {t}) mod {n} = {current_sequence_value}")
            sequence.append(current_sequence_value)
        print()

    return is_prime


assert repeated_squaring_modular_exponentiation(42, 51, 73) == 17


def choose_value():
    if len(sys.argv) != 2:
        return 3017
    else:
        try:
            return int(sys.argv[1])
        except ValueError:
            raise RuntimeError(f"Usage: {sys.argv[0]} [number]")


if __name__ == '__main__':
    print(f"Miller-Rabin: {miller_rabin(choose_value())}")
    print(f"Don't trust me? Try a Miller-Rabin calculator https://planetcalc.com/8995/")
