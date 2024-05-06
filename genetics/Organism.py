from random import randint
from utils import Point, chance

class Organism:
    def __init__(self, genome: list[str]) -> None:
        self.internal_mutation_probability = 0.6 # mutation probability for gene in genome (should be in config)
        self.gene_length = 0
        self.genome = genome
    
    # convert binary gene to direction
    def phenotype(self, gene: str) -> Point: 
        return Point(0,0)
        # return directions[gene]
    
    # convert genome into coordinate point
    def phenome(self) -> Point:
        current_location = Point(0, 0)
        for gene in self.genome:
            current_location.add(self.phenotype(gene))
        return current_location
    
    # create random gene with n bits
    def random_gene(self, length):
        gene = []
        for _ in range(length):
            gene.append(randint(0, 1))
        return ''.join(map(str, gene))
    
    def fitness(self):
        pass
    

    # mutate genome by randomly changing bits in genome
    def mutate(self):
        for (gene_index, gene) in enumerate(self.genome): # less computation but still lot's of variety
            if(chance(self.internal_mutation_probability)):
                # choose a random bit and flip it's value
                gene_str = list(gene)
                bit_index = randint(0, 0) # todo: dynamic gene length
                gene_str[bit_index] = str((1 if int(gene_str[bit_index]) == 0 else 0))
                self.genome[gene_index] = "".join(gene_str)