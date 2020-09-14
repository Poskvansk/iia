import random

# 0 - SP
# 1 - BA
# 2 - RJ
# 3 - Lima
# 4 - Bog.
# 5 - Sant.
# 6 - Carac.
# 7 - BH
# 8 - PoA
# 9 - BsB

#matriz distancia, igual PDF

dist_matrix = [ [0, 17, 3, 35, 43, 26, 44, 5, 8, 9],
                [0, 0, 20, 31, 47, 11, 51, 22, 8, 23],
                [0, 0, 0, 38, 45, 29, 45, 3, 11, 9],
                [0, 0, 0, 0, 19, 25, 27, 36, 33, 32],
                [0, 0, 0, 0, 0, 43, 10, 43, 46, 37],
                [0, 0, 0, 0, 0, 0, 49, 30, 19, 30],
                [0, 0, 0, 0, 0, 0, 0, 42, 48, 35],
                [0, 0, 0, 0, 0, 0, 0, 0, 13, 6],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 16],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ]


class Individual:

    def calculate_distance(self, i, j):
        if(j < i):
            i, j = j, i
        return dist_matrix[i][j]

    def calculate_total_distance(self, genome):
        
        total_distance = 0
        
         #calcula a distancia de gnome[i] + genome[i+1]
        
        for i in range(0, len(genome)-1):
            total_distance = total_distance + self.calculate_distance(genome[i], genome[i+1])
        return total_distance

    def __init__(self, genome = None):
      
        self.genome = genome
        
        #gera vetor aleatorio, primeiro e ultimo elementos sempre = 9  (codigo de BsB)
        if self.genome is None:
            self.genome = [9] + random.sample(range(0,9), 9) + [9]
        
        #calcula a distancia total do caminho
        self.total_distance = self.calculate_total_distance(self.genome)