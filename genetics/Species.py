from typing import Type, TypeVar, Generic, Dict
from random import randint
import math
from utils import chance, random_exclude
from genetics.MazeBuilder import MazeBuilder
from genetics.MazeSolver import MazeSolver

O = TypeVar('O', MazeBuilder, MazeSolver) # species type

class Species(Generic[O]):

    # initialize organisms to start evolving
    def __init__(self, genetic_config: Dict[str, int], organism_class: Type[O]) -> None:
        self.n_organisms = genetic_config['n_organisms']
        self.organisms: list[O] = []
        self.organism_class = organism_class
        self.generation = 0
        self.tournament_proportion = genetic_config['tournament_proportion']
        self.mutation_probability = genetic_config['mutation_probability']
        self.genesis()

    # progress to next generation
    def evolve(self):
        # tournament selection -> crossover -> mutation
        self.generation += 1
        # select % of population to duel, winners crossover, losers removed from pool
        candidates: list[O] = []

        # tournament selection for crossover candidates
        for _ in range(math.floor((self.n_organisms * self.tournament_proportion) / 2)):
            p1_index = randint(0, len(self.organisms) - 1)
            participant1 = self.organisms[p1_index] 
            p2_index = random_exclude(p1_index)
            participant2 = self.organisms[p2_index]

            # whoever has better fitness is added to candidate pool, loser is removed from species
            if(participant1.fitness() < participant2.fitness()):
                candidates.append(participant1)
                self.organisms.pop(p2_index)
            else:
                candidates.append(participant2)
                self.organisms.pop(p1_index)

        # uneven number of candidates, add 1 
        if(len(candidates) % 2 != 0):
            candidates.append(self.organisms[randint(0, len(self.organisms) - 1)])

        candidate_middle_index = int(len(candidates) / 2)

        # crossover for all pairs of candidates
        for (parent1, parent2) in zip(candidates[:candidate_middle_index], candidates[candidate_middle_index:]):
            self.crossover(parent1, parent2)

    
    # split genome in random place and combine with chance of mutation 
    def crossover(self, parent1: O, parent2: O):
        top_range = min(len(parent1.genome), len(parent2.genome)) # parents can have diff number of genes
        position = randint(0, top_range) 

        parent1_genome_str = "".join(parent1.genome)
        parent2_genome_str = "".join(parent2.genome)
        (parent1_l_genome,parent1_r_genome) = (parent1_genome_str[:position], parent1_genome_str[position:])
        (parent2_l_genome,parent2_r_genome) = (parent2_genome_str[:position], parent2_genome_str[position:])

        # created 2 children (with chance of mutation) from spliced genome
        for combined_genome in ([parent1_l_genome + parent2_r_genome, parent2_l_genome + parent1_r_genome]):
            child = self.organism_class([combined_genome[i] for i in range(0, len(combined_genome), 1)]) # todo: dynamic gene length
            if chance(self.mutation_probability):
                child.mutate()
            self.organisms.append(child)

    # find the most fit organism from pool
    def best(self):
        best = self.organisms[0]
        for organism in self.organisms:
            if organism.fitness() < best.fitness():
                best = organism

        return best

    # check if the best organism's phenotype matches the target color
    def reached_solution(self):
        #todo: change
        return self.best().fitness() == 0
    
    # initiate a new set of generations
    def genesis(self):
        self.generation = 0
        self.organisms = []
        for _ in range(self.n_organisms):
            self.organisms.append(self.organism_class())