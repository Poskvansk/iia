from individual import *

def cross(p1, p2):

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

    indiv = Individual(aux)
    indiv.total_distance = indiv.calculate_total_distance(indiv.genome)

    return indiv

def crossover(population):
    
    sons = []
    
    #cruza os individuos da população
    #individuo[i] cruza com individuo[i+1]
    for i in range(0, len(population)-2):
        j = 1

        #evita a reprodução entre dois individuos com mesmo genoma (que resultaria em mais um clone)
        #se individuo[i] tem mesmo genoma que individuo[i+1], indivudo[i] cruzara com individuo[i+j], 1 < j, ate que sejam diferentes
        while(population[i].genome == population[i+j].genome) and (population[i+j] != population[-1]):
            j+=1

        aux = cross(population[i], population[i+j])
        sons.append(aux)

    return sons
     
########################################################################################################
# def crossover(population):
    
#     sons = []
    
#     #cruza os individuos da população
#     #individuo[i] cruza com individuo[i+1]
#     #individuo[i+1] NAO cruza com individuo [i+2]
#     for i in range(0, len(population)):
#         if(i % 2 == 0) and (population[i] != population[-1]):
#             #for anda de 2 em 2
#             aux = cross(population[i], population[i+1])
#             sons.append(aux)

#     for i in range(0, len(population)):
#         if(i % 2 == 0) and (population[i] != population[-1]):
#             #for anda de 2 em 2
#             aux = cross(population[i+1], population[i])
#             sons.append(aux)
#     return sons

########################################################################################################
