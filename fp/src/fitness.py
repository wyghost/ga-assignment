def onemax_fitness(chromosome):
    return sum(chromosome)


def knapsack_fitness(chromosome, values, weights, capacity):
    total_value = sum(bit * value for bit, value in zip(chromosome, values))
    total_weight = sum(bit * weight for bit, weight in zip(chromosome, weights))

    if total_weight > capacity:
        return 0

    return total_value