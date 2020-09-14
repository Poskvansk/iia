import random

def mutate(population):
    
    for i in population:
        chance = random.randrange(0, 100)/100
        #para cada individuo, vai tirar um numero enrtre 0 e 1
        if(chance < 0.2):
            #se o numero for menor que 0.2, nesse caso, vai ocorrer mutacao
            
            #idx1 vai ser um numero entre 1 e 10 (as posicoes no genoma)
            idx1 = random.randrange(1,10)
            idx2 = idx1

            while idx2 == idx1: 
                #idx2 vai ser numero entre 1 e 10, diferente de idx1
                idx2 = random.randrange(1,10)             
            
            #swapa os 2
            i.genome[idx1], i.genome[idx2] = i.genome[idx2], i.genome[idx1]
            i.total_distance = i.calculate_total_distance(i.genome)        