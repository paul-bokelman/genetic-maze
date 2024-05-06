from random import randint
from tkinter import ttk as tk, Tk, Canvas
from maze import Maze, cell_identifiers, cells
from genetics.Species import Species
from genetics.MazeBuilder import MazeBuilder
from utils import Point, chance
from config import sim_config, builder_species_config

dimensions = builder_species_config['maze_size'] * sim_config['cell_size'] + 1.5 * sim_config['padding']

maze_builder_species = Species(builder_species_config, MazeBuilder)


root = Tk()
root.title('Genetic Maze')

canvas = Canvas(root, bg='#212121', width=dimensions, height=dimensions)
generation_label = tk.Label(root, text=f"Generation 0, Best: {maze_builder_species.best().fitness()}")
generation_label.pack()

def simulate_organisms():
  global current_after_id
  canvas.delete('all')

  for row in range(builder_species_config['maze_size']):
    for col in range(builder_species_config['maze_size']):
      x = sim_config['padding'] + sim_config['cell_size'] * col
      y = sim_config['padding'] + sim_config['cell_size'] * row
      canvas.create_rectangle(x, y, x + sim_config['cell_size'], y + sim_config['cell_size'], fill='#212121', outline='#212121')


  generation_label.config(text=f"Generation {maze_builder_species.generation}, Best: {maze_builder_species.best().fitness()}")

  best = maze_builder_species.best()

  row = 0
  col = 0

  for gene in best.genome:
      cell = cell_identifiers[gene]
     
      x = sim_config['padding'] + (sim_config['cell_size']) * col
      y = sim_config['padding'] + (sim_config['cell_size']) * row

      canvas.create_rectangle(x, y, x + sim_config['cell_size'], y + sim_config['cell_size'], fill=cell['color'], outline=cell['color'])
      if((sim_config['padding'] + (sim_config['cell_size']) * (col + 1)) + sim_config['cell_size'] >= dimensions):
          row += 1
          col = 0
      else: 
          col += 1
    

  # if a solution has been reached, stop the sim and display in console
  if not maze_builder_species.reached_solution():
      id = canvas.after(sim_config['evo_delay'], simulate_organisms)
      current_after_id = id
      maze_builder_species.evolve() 
  else:
      print(f'Solution reached after {maze_builder_species.generation} generation(s)')


simulate_organisms() 
canvas.pack()

root.mainloop()

