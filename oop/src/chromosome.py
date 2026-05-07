from dataclasses import dataclass
from typing import List


@dataclass
class Chromosome:
    genes: List[int]
    fitness: float = 0.0

    def copy(self) -> "Chromosome":
        return Chromosome(self.genes[:], self.fitness)