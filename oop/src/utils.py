import random


def random_bitstring(length: int):
    return [random.randint(0, 1) for _ in range(length)]