from abc import ABC, abstractmethod
import random
from chromosome import Chromosome


class CrossoverStrategy(ABC):
    @abstractmethod
    def crossover(self, parent1: Chromosome, parent2: Chromosome):
        pass


class OnePointCrossover(CrossoverStrategy):
    def __init__(self, probability: float = 0.9):
        self.probability = probability

    def crossover(self, parent1: Chromosome, parent2: Chromosome):
        length = len(parent1.genes)

        if random.random() > self.probability:
            return parent1.copy(), parent2.copy()

        point = random.randint(1, length - 1)

        child1_genes = parent1.genes[:point] + parent2.genes[point:]
        child2_genes = parent2.genes[:point] + parent1.genes[point:]

        return Chromosome(child1_genes), Chromosome(child2_genes)