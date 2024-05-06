from typing import Optional
import math
from config import builder_species_config
from genetics.Organism import Organism
from utils import Point

# 1 is open, 0 is closed

class Grid:
    def __init__(self, genome: list[str]) -> None:
        self.grid = [[]]
        self.points_indexed: list[Point] = []

        row = 0
        col = 0
        for gene in genome:
            self.grid[row].append(gene)
            col += 1
            if col == builder_species_config['maze_size']:
                 if row != builder_species_config['maze_size'] - 1:
                    self.grid.append([])
                 row +=1
                 col = 0

    # find all islands on grid, return as list with # of components in each as entries
    def find_islands(self) -> list[int]:
        islands = []


        for (row_index, row) in enumerate(self.grid):
            for (col_index, gene) in enumerate(row):
                # can't be an island because islands are only walls
                point = Point(col_index, row_index)
                if gene == "1": 
                    self.points_indexed.append(point)
                    continue                         

                # find all neighbors of wall
                if point not in self.points_indexed:
                    island_size = self.search_island(point)
                    islands.append(island_size)

                self.points_indexed.append(point)

        return islands

    def search_island(self, point: Point):
        n_nodes = 1

        for indexed_point in self.points_indexed:
            if indexed_point.__eq__(point):
                return n_nodes

        self.points_indexed.append(point)

        # print(f"For point", point.x, point.y)
        for neighbor in point.neighbors(builder_species_config['maze_size']):
            if neighbor in self.points_indexed or self.grid[neighbor.y][neighbor.x] == "1":
                continue
            # print("valid neighbor: ", neighbor.x, neighbor.y)

            n_nodes += self.search_island(neighbor)

        return n_nodes


# inherits Organism but with unique fitness function
class MazeBuilder(Organism):
    def __init__(self, genome: Optional[list[str]] = None) -> None:
        self.genome = []
        self.gene_length = 2

        # fitness factors
        self.distance_factor = 1.2
        self.step_factor = 0

        if genome != None :
            self.genome = genome
        else:
            for _ in range(int(math.pow(builder_species_config['maze_size'], 2))):
                    self.genome.append("1") # gene size of 2 (represents 4 states)

        super().__init__(self.genome)


    def fitness(self):
        score = 2

        grid = Grid(self.genome)
        islands = grid.find_islands()
            
        # check length of whole (neighbors)
        # number of islands, length of islands

        
        score = score - len(islands)

        for island in islands:
            if island <= 5:
                score = score - island
            else:
                score = score + island

        # rules for fitness

        return score