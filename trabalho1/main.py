from individual import *

def createPopulation():
    population = []
    for i in range(0,10):
        aux = Individual()
        population.append(aux)
    return population

def cross(p1, p2):

    indiv = Individual()
    aux = []
    for i in p1.genome[:3]:
        aux.append(i)

    for i in p2.genome[3:]:
        while i in aux and i != aux[0]:
            i += 1
            i %= 9
        aux.append(i)

    indiv.genome = aux
    indiv.total_distance = indiv.calculate_total_distance(indiv.genome)

    return indiv

def crossover(population):
    
    sons = []
    for i in range(0, len(population)):
        if(i % 2 == 0) and (population[i] != population[-1]):
            aux = cross(population[i], population[i+1])
            sons.append(aux)

    return sons

def sortDist(val):
    return val.total_distance
 

def print_pop(population):
    for i in range(0, len(population)):
        print(population[i].genome, "->", population[i].total_distance)


def discard_worst(population):
    i = len(population) - 1

    while i > len(population)/2 :
        population.pop()
        i -= 1


def mutate(population):
    for i in population:
        chance = random.randrange(0, 100)/100

        if(chance < 0.9):
            idx1 = random.randrange(1,10)
            idx2 = idx1

            while idx2 == idx1: 
                idx2 = random.randrange(1,10)

            i.genome[idx1], i.genome[idx2] = i.genome[idx2], i.genome[idx1]
            i.total_distance = i.calculate_total_distance(i.genome)        

def main():

    population = createPopulation()
    population.sort(key=sortDist)    

    print_pop(population)

    i = 0
    while i < 10 :
        print("========================= GENERATION ", i, "=========================")
        new_gen = crossover(population)
        mutate(new_gen)
        
        # print_pop(new_gen)

        discard_worst(population)

        population = population + new_gen
        population.sort(key=sortDist)

        print("Results")
        print_pop(population)
        i+=1


main()