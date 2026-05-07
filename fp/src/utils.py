import random


def random_bitstring(length):
    return [random.randint(0, 1) for _ in range(length)]


def create_population(population_size, chromosome_length):
    return [random_bitstring(chromosome_length) for _ in range(population_size)]