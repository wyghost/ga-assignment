from abc import ABC, abstractmethod
import random
from chromosome import Chromosome


class MutationStrategy(ABC):
    @abstractmethod
    def mutate(self, chromosome: Chromosome) -> Chromosome:
        pass


class BitFlipMutation(MutationStrategy):
    def __init__(self, probability_per_bit: float):
        self.probability_per_bit = probability_per_bit

    def mutate(self, chromosome: Chromosome) -> Chromosome:
        new_genes = chromosome.genes[:]

        for i in range(len(new_genes)):
            if random.random() < self.probability_per_bit:
                new_genes[i] = 1 - new_genes[i]

        return Chromosome(new_genes)