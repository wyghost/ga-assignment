import random
import time

from utils import create_population


def evaluate_population(population, fitness_function):
    return [fitness_function(chromosome) for chromosome in population]


def best_individual(population, fitnesses):
    best_index = max(range(len(population)), key=lambda i: fitnesses[i])
    return population[best_index][:], fitnesses[best_index]


def tournament_select(population, fitnesses, k=3):
    indices = random.sample(range(len(population)), k)
    winner_index = max(indices, key=lambda i: fitnesses[i])
    return population[winner_index][:]


def one_point_crossover(parent1, parent2, probability=0.9):
    length = len(parent1)

    if random.random() > probability:
        return parent1[:], parent2[:]

    point = random.randint(1, length - 1)

    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]

    return child1, child2


def bit_flip_mutation(chromosome, probability_per_bit):
    return [
        (1 - gene) if random.random() < probability_per_bit else gene
        for gene in chromosome
    ]


def next_generation(
    population,
    fitnesses,
    elitism_count,
    crossover_probability,
    mutation_probability,
    fitness_function,
):
    ranked = sorted(
        zip(population, fitnesses),
        key=lambda pair: pair[1],
        reverse=True
    )

    new_population = [chromosome[:] for chromosome, _ in ranked[:elitism_count]]

    while len(new_population) < len(population):
        parent1 = tournament_select(population, fitnesses, k=3)
        parent2 = tournament_select(population, fitnesses, k=3)

        child1, child2 = one_point_crossover(parent1, parent2, crossover_probability)

        child1 = bit_flip_mutation(child1, mutation_probability)
        child2 = bit_flip_mutation(child2, mutation_probability)

        new_population.append(child1)
        if len(new_population) < len(population):
            new_population.append(child2)

    return new_population


def run_ga(
    chromosome_length,
    population_size,
    generations,
    elitism_count,
    crossover_probability,
    mutation_probability,
    fitness_function,
):
    start_time = time.time()

    population = create_population(population_size, chromosome_length)
    fitnesses = evaluate_population(population, fitness_function)

    fitness_history = []

    for _ in range(generations):
        population = next_generation(
            population=population,
            fitnesses=fitnesses,
            elitism_count=elitism_count,
            crossover_probability=crossover_probability,
            mutation_probability=mutation_probability,
            fitness_function=fitness_function,
        )

        fitnesses = evaluate_population(population, fitness_function)
        _, best_fitness = best_individual(population, fitnesses)
        fitness_history.append(best_fitness)

    best_genes, best_fitness = best_individual(population, fitnesses)
    runtime = time.time() - start_time

    return {
        "best_fitness": best_fitness,
        "best_genes": best_genes,
        "fitness_history": fitness_history,
        "runtime_seconds": runtime,
    }