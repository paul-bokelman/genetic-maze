from typing import Optional
import math
from config import solver_species_config
from genetics.Organism import Organism
from utils import Point

# inherits Organism but with unique fitness function    
class MazeSolver(Organism):
    def __init__(self, genome: Optional[list[str]] = None) -> None:
        self.gene_length = 2
        super().__init__(self.genome)    
        # fitness factors
        self.distance_factor = 1.2
        self.step_factor = 0

    def fitness(self):
        score = 0
        current_location = super().phenome()
        distance = current_location.distance(Point(24, 24)) #todo: dynamic endpoint
        steps = len(self.genome)

        # should try and optimize 0 for readability but it's ok for now
        score = self.distance_factor * distance + self.step_factor * steps
        return score