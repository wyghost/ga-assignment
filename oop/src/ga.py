import random
import time
from chromosome import Chromosome
from population import Population
from utils import random_bitstring


class GeneticAlgorithm:
    def __init__(
        self,
        chromosome_length,
        population_size,
        generations,
        elitism_count,
        selection_strategy,
        crossover_strategy,
        mutation_strategy,
        fitness_function,
    ):
        self.chromosome_length = chromosome_length
        self.population_size = population_size
        self.generations = generations
        self.elitism_count = elitism_count
        self.selection_strategy = selection_strategy
        self.crossover_strategy = crossover_strategy
        self.mutation_strategy = mutation_strategy
        self.fitness_function = fitness_function

    def initialize_population(self) -> Population:
        individuals = []
        for _ in range(self.population_size):
            genes = random_bitstring(self.chromosome_length)
            individuals.append(Chromosome(genes))
        return Population(individuals)

    def evaluate_population(self, population: Population):
        for chromosome in population.individuals:
            chromosome.fitness = self.fitness_function(chromosome)

    def run(self):
        start_time = time.time()

        population = self.initialize_population()
        self.evaluate_population(population)

        fitness_history = []

        for _ in range(self.generations):
            next_generation = []

            elites = population.sorted_by_fitness_desc()[:self.elitism_count]
            next_generation.extend([elite.copy() for elite in elites])

            while len(next_generation) < self.population_size:
                parent1 = self.selection_strategy.select(population)
                parent2 = self.selection_strategy.select(population)

                child1, child2 = self.crossover_strategy.crossover(parent1, parent2)

                child1 = self.mutation_strategy.mutate(child1)
                child2 = self.mutation_strategy.mutate(child2)

                next_generation.append(child1)
                if len(next_generation) < self.population_size:
                    next_generation.append(child2)

            population = Population(next_generation)
            self.evaluate_population(population)

            best_fitness = population.best().fitness
            fitness_history.append(best_fitness)

        runtime = time.time() - start_time
        best_solution = population.best()

        return {
            "best_fitness": best_solution.fitness,
            "best_genes": best_solution.genes,
            "fitness_history": fitness_history,
            "runtime_seconds": runtime,
        }