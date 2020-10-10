
class Paciente():

    neonato = 0

    temp_corpo = 0
    dias_febre = 0

    # manchas = 0
    mancha_freq = 0

    dor_musc_freq = 0

    dor_art_freq = 0
    dor_art_intensidade = 0

    edema_art = 0
    edema_intd = 0

    conjuntivite = 0

    dor_cabeca_freq = 0
    dor_cabeca_intd = 0

    coceira = 0

    hiptrof_gangli_freq = 0
    disc_hemo = 0
    acomet_neuro = 0


def getStatusPaciente(paciente):

    paciente.temp_corpo = float(input("Qual a temperatura corporal? "))

    if paciente.temp_corpo > 38.0:
        paciente.dias_febre = int(input("Por quantos dias observou-se a febre? "))

    # # aux = input("Manchas na pele? (s/n) ")
    # # if aux[0] == 's': 
    #     #  paciente.manchas = 1
    # paciente.manchas_freq = int(input("A partir de quantos dias observou-se as manchas? "))

    paciente.dor_musc_freq = int(input("De 0 a 10, qual a frequencia da dor muscular? "))
    
    paciente.dor_art_freq = int(input("De 0 a 10, qual a frequencia da dor articular? "))
    paciente.dor_art_intd = int(input("De 0 a 10, qual a intensidade da dor articular? "))

    aux = input("Ocorreu edema da articulação? (s/n) ")
    if aux[0] == 's': 
        paciente.edema_art = 2
        paciente.edema_intd = int(input("De 1 a 10, qual a intensidade do edema? "))

    aux = input("Houve conjuntivite? (s/n) ")
    if aux[0] == 's': 
        paciente.conjuntivite = 2

    # aux = input("Houve dor de cabeça? (s/n)")
    # if aux[0] == 's': 
    #     paciente.dor_cabeca_freq = 1

    #     paciente.dor_cabeca_intd = int(input("De  a 10, qual a intensidade da dor de cabeça? "))

    paciente.coceira = int(input("De 0 a 10, qual a intensidade da coceira? "))

    paciente.hiptrof_gangli_freq= int(input("De 0 a 10, com que frequencia esta ocorrendo hipertrofia ganglionar? "))

    aux = input("Houve discrasia hemorrágica? (s/n) ")
    if aux[0] == 's': 
        paciente.disc_hemo = 2

    aux = input("Houve acometimento neurológico? (s/n) ")
    if aux[0] == 's': 
        paciente.acomet_neuro = 2
        
        neo = input("O paciente é neonato? (s/n) ")
        if neo[0] == 's':
            paciente.neonato = 2

    return paciente