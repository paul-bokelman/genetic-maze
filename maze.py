from typing import Optional
from utils import Point, chance

maze_builder_genetics = {
   "n_organisms": 600,
    "tournament_proportion": 0.8, 
    "mutation_probability": 0.4,  
}

cells = {
    "start": {"char": "s", "color": "#32a852"},
    "end": {"char": "e", "color": "#8a42f5"},
    "open": {"char": "o", "color": "#fff"},
    "closed": {"char": "c", "color": "#000"},
}

cell_identifiers = {
    # "00": cells["start"],
    # "01": cells["end"],
    # "10": cells["open"],
    # "11": cells["closed"],

    # "00": cells["start"],
    # "01": cells["end"],
    "1": cells["open"],
    "0": cells["closed"]
}

directions = {
    "00": Point(0, -1),
    "01": Point(1, 0),
    "10": Point(-1, 0),
    "11": Point(0, 1)
}

class Cell(Point):
    def __init__(self, point:tuple[int, int], id: Optional[str] = None) -> None:
        obj = cells['closed']
        if id:
            obj = cells[id]

        self.char = obj['char']
        self.color = obj['color']
        super().__init__(point[0], point[1])

    def convert(self, id: str):
        obj = cells[id]
        self.char = obj['char']
        self.color = obj['color']

class Maze:
    def __init__(self, size) -> None:
        self.maze: list[list[Cell]] = []
        self.size = size
        self.generate()

    def generate(self):
    # plot solution, create complications from solution path

        # generate all cells
        for y in range(self.size):
            row = []
            for x in range(self.size):
                    cell = Cell((x, y))
                    row.append(cell)
            
            self.maze.append(row)

        

        # # convert start and end cells
        # self.maze[0][0].convert('start')
        # self.maze[self.size - 1][self.size - 1].convert('end')
        

        # find solution

# running = True
# maze_builder_species = Species(maze_builder_genetics, MazeBuilder)
# while running:
#     maze_builder_species.evolve()
#     best = maze_builder_species.best()
#     print('generation', maze_builder_species.generation)
#     print(best.fitness())
#     if(best.fitness() == 0):
#         print(best.genome)