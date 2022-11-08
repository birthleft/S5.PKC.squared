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
    print(f"t = {bin(t)[2:]} = {number_as_sum_of_powers_of_2(t)}. powers of 2: {list([i for i in range(t.bit_length()) if is_set(t, i)])}")
    print()
    for i in range(0, t.bit_length()):
        print(f"2^(2^{i}) = {2 ** 2 ** i % n}", end=' ')
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

    is_prime = True
    for a in [2, 3, 5]:
        sequence = []
        print(f"a = {a}")

        # we need to compute a^t, a^(2t), a^(4t), ..., a^(2^s * t)
        for r in range(s + 1):  # 0, 1, 2, ..., s. Why? Step 2 of https://moodle.cs.ubbcluj.ro/pluginfile.php/46227/mod_resource/content/1/pkc-c03.pdf#page=20
            current_sequence_element = 'x' if not is_prime or (r == s and sequence[r - 1] != -1) else repeated_squaring_modular_exponentiation(a, 2 ** r * t, n)
            current_sequence_element = -1 if type(current_sequence_element) == int and current_sequence_element + 1 == n else current_sequence_element
            sequence.append(current_sequence_element)
            print(f"{a}^(2 ^ {r} * {t}) = {current_sequence_element}")

        # checking if neither the 2nd condition is met
        if is_prime and sequence[-1] != 1:
            is_prime = False

    return is_prime


assert repeated_squaring_modular_exponentiation(42, 51, 73) == 17

if __name__ == '__main__':
    value = int(sys.argv[1]) if len(sys.argv) == 2 else 5521
    print(f"Miller-Rabin: {miller_rabin(value)}")
    print(f"Don't trust me? Try a Miller-Rabin calculator https://planetcalc.com/8995/")
