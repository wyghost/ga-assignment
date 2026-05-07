from typing import List
from chromosome import Chromosome


class Population:
    def __init__(self, individuals: List[Chromosome]):
        self.individuals = individuals

    def size(self) -> int:
        return len(self.individuals)

    def best(self) -> Chromosome:
        return max(self.individuals, key=lambda c: c.fitness)

    def sorted_by_fitness_desc(self) -> List[Chromosome]:
        return sorted(self.individuals, key=lambda c: c.fitness, reverse=True)