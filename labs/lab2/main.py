
def is_generator(order, g):
    # https://en.wikipedia.org/wiki/Cyclic_group#:~:text=Definition%20and%20notation,-The%20six%206th&text=The%20order%20of%20g%20is,called%20a%20generator%20of%20G.
    generated = set()
    for k in range(0, order):
        generated.add(k * g % order)

    return len(generated) == order


def find_generators(order):
    generators = set()

    for g in range(0, order):
        if is_generator(order, g):
            generators.add(g)

    return generators


if __name__ == '__main__':
    for n in range(2, 100):
        print(f'Generators of the cyclic group Z_{n}: {find_generators(n)}')
