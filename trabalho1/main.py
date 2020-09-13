from individual import *


#cria populacao de N individuos range(0,N)
def createPopulation():
    population = []
    for i in range(0,10):
        aux = Individual()
        population.append(aux)
    return population

def cross(p1, p2):

    indiv = Individual()
    aux = []
    
    #append os 3 primeiros elementos do genoma de p1
    for i in p1.genome[:3]:
        aux.append(i)

    #append os elementos a partir do terceiro do genoma P2
    for i in p2.genome[3:]:
        #Para cada elemento i do genoma p2, enquanto i ja estiver presente no genoma aux do filho, i++
        while i in aux and i != aux[0]:
            i += 1
            
            #i % 9 garante que 0 <= i < 9
            i %= 9
        aux.append(i)
        
    indiv.genome = aux
    indiv.total_distance = indiv.calculate_total_distance(indiv.genome)

    return indiv

def crossover(population):
    
    sons = []
    
    #cruza os individuos da população
    #individuo[i] cruza com individuo[i+1]
    #individuo[i+1] NAO cruza com individuo [i+2]
    for i in range(0, len(population)):
        if(i % 2 == 0) and (population[i] != population[-1]):
            #for anda de 2 em 2
            aux = cross(population[i], population[i+1])
            sons.append(aux)

    return sons

def sortDist(val):
    #ordena populacao usando a distancia total como parametro
    return val.total_distance
 

def print_pop(population):
    #printa a populacao atual
    #[genoma] -> distancia total    
    for i in range(0, len(population)):
        print(population[i].genome, "->", population[i].total_distance)


def discard_worst(population):
    i = len(population) - 1
    #discarda N/2 os piores individuos da população
    #os 50% mais lentos vao ser descartados sem piedade
    while i > len(population)/2 :
        population.pop()
        i -= 1


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

def main():
    
    #cria populacao
    #ordena os individuos por distancia
    population = createPopulation()
    population.sort(key=sortDist)    

    print_pop(population)

    i = 0
    while i < 10 :
        print("========================= GENERATION ", i, "=========================")
        
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

        print("Results")
        print_pop(population)
        i+=1


main()
