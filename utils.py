from typing import Type, Self
import math
from random import randint


class Point:
  def __init__(self, x: int, y: int) -> None:
      self.x = x
      self.y = y
  def add(self, point: Self):
      self.x += point.x
      self.y += point.y
  def distance(self, point: Self):
     return math.sqrt( math.pow(self.x - point.x, 2) + math.pow(self.y - point.y, 2))
  
  # check to see if point lays inside grid
  def is_invalid(self, grid_size):
     if self.x < 0 or self.y < 0:
        return True
     if self.x >= grid_size or self.y >= grid_size:
        return True
  
  # computes valid possible neighbors 
  def neighbors(self, grid_size) -> list[Self]:
    neighbors = []

    possible_neighbors = [Point(self.x -1, self.y), Point(self.x, self.y - 1), Point(self.x + 1, self.y), Point(self.x, self.y + 1)]

    for possible_neighbor in possible_neighbors:
       if not possible_neighbor.is_invalid(grid_size):
          neighbors.append(possible_neighbor)
          
    return neighbors
     
  def get_coords(self):
     return (self.x, self.y)
  def __eq__(self, point: Self) -> bool:
      return self.x == point.x and self.y == point.y
      

def random_exclude(*exclude):
  exclude = set(exclude)
  randInt = randint(0,9)
  return random_exclude(*exclude) if randInt in exclude else randInt 

def chance(probability: float):
   return randint(1, 10) <= probability * 10