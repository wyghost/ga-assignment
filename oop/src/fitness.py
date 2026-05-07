from chromosome import Chromosome


def onemax_fitness(chromosome: Chromosome) -> int:
    return sum(chromosome.genes)


def knapsack_fitness(chromosome: Chromosome, values, weights, capacity) -> int:
    total_value = 0
    total_weight = 0

    for bit, value, weight in zip(chromosome.genes, values, weights):
        if bit == 1:
            total_value += value
            total_weight += weight

    if total_weight > capacity:
        return 0

    return total_value