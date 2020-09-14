from individual import *
from mutate import *
from crossover import *

#cria populacao de N individuos range(0,N)
def createPopulation():
    population = []
    for i in range(0,50):
        aux = Individual()
        population.append(aux)
    return population

def sortDist(val):
    #ordena populacao usando a distancia total como parametro
    return val.total_distance
 
def print_pop(population):
    #printa a populacao atual
    #[genoma] -> distancia total
    for i in range(0, len(population)):
        print(population[i].genome, "->", population[i].total_distance)

def print_best(population):
    for i in range(0, 2):
        print(population[i].genome, "->", population[i].total_distance)

def discard_worst(population):
    i = len(population) - 1
    #discarda N/2 os piores individuos da população
    #os 50% mais lentos vao ser descartados sem piedade
    while i > len(population)/2 :
        population.pop()
        i -= 1

def main():
    
    #cria populacao
    #ordena os individuos por distancia
    population = createPopulation()
    population.sort(key=sortDist)    

    print("Population size = ", len(population))
    print_pop(population)

    i = 0
    while i < 1000 :
        print("========================= GENERATION ", i+1  , "=========================")
        
        #cria uma geracao de filhos
        new_gen = crossover(population)
        #muta geracao filhos
        mutate(new_gen)
        
        # print_pop(new_gen)
        
        #descarta os piores sem piedade
        discard_worst(population)
        
        #junta a populacao dos melhores pais com os novos filhos
        population = population + new_gen
        
        #ordena
        population.sort(key=sortDist)

        print("Population size = ", len(population))
        # print_pop(population)
        print("Now the best are:  ")
        print_best(population)
        i+=1

main()
