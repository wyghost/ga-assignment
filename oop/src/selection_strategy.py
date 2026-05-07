from abc import ABC, abstractmethod
import random
from population import Population
from chromosome import Chromosome


class SelectionStrategy(ABC):
    @abstractmethod
    def select(self, population: Population) -> Chromosome:
        pass


class TournamentSelection(SelectionStrategy):
    def __init__(self, k: int = 3):
        self.k = k

    def select(self, population: Population) -> Chromosome:
        contestants = random.sample(population.individuals, self.k)
        winner = max(contestants, key=lambda c: c.fitness)
        return winner.copy()