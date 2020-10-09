import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

class Paciente():

    idade = 0

    temp_corpo = 0
    dias_febre = 0

    # manchas = 0
    mancha_freq = 0

    dor_musc_freq = 0

    dor_art_freq = 0
    dor_art_intensidade = 0

    edema_art = 0
    edema_art_intd = 0

    conjuntivite = 0

    dor_cabeca_freq = 0
    dor_cabeca_intd = 0

    coceira = 0

    hiptrof_gangli_freq = 0
    disc_hemo = 0
    acomet_neuro = 0

def getStatusPaciente(paciente):

    paciente.temp_corpo = int(input("Qual a temperatura corporal? "))
    paciente.dias_febre = int(input("Por quantos dias observou-se a febre? "))

    # # aux = input("Manchas na pele? (s/n) ")
    # # if aux[0] == 's': 
    #     #  paciente.manchas = 1
    # paciente.manchas_freq = int(input("A partir de quantos dias observou-se as manchas? "))

    paciente.dor_musc_freq = int(input("De 0 a 10, quão alta é a frequencia da dor muscular? "))
    
    # paciente.dor_art_freq = int(input("De 0 a 10, quão alta é a frequencia da dor articular? "))
    # paciente.dor_art_intd = int(input("De 0 a 10, quão alta é a intensidade da dor articular? "))

    # aux = input("Ocorreu edema da articulação? (s/n) ")
    # if aux[0] == 's': 
    #     paciente.edema_art = 1

    # paciente.edema_intd = input("De 0 a 10, qual a intensidade do edema? ")

    # aux = input("Houve conjuntivite? (s/n) ")
    # if aux[0] == 's': 
    #     paciente.conjuntivite = 1

    # aux = input("Houve dor de cabeça? (s/n)")
    # if aux[0] == 's': 
    #     paciente.dor_cabeca_freq = 1

    # paciente.dor_cabeca_intd = int(input("De 0 a 10, qual a intensidade da dor de cabeça? "))

    # paciente.coceira = input("De 0 a 10, qual a intensidade da coceira? ")

    # aux = input("Houve hipertrofia ganglionar? (s/n) ")
    # if aux[0] == 's': 
    #     paciente.hiptrof_gangli_freq = 1


    # paciente.disc_hemo = input("Houve discrasia hemorrágica? (s/n) ")

    # paciente.acomet_neuro = input("Houve acometimento neurológico? (s/n) ")

    # paciente.idade = int(input("Qual a idade do paciente? "))

    return paciente

def main():

    p1 = Paciente()
    p1 = getStatusPaciente(p1)

    febre = ctrl.Antecedent(np.arange(36, 40.5, 0.5), 'febre')
    dias_febre = ctrl.Antecedent(np.arange(0, 8, 1), 'dias_febre')

    # manchas = 
    # mancha_freq = ctrl.Antecedent(np.arange(0,8), 'dia aparicao mancha')

    dor_musc_freq = ctrl.Antecedent(np.arange(0,11), 'dor_musc_freq')

    # dor_art_freq = ctrl.Antecedent(np.arange(0, 11), 'Freq. dor artic.')
    # dor_art_intensidade = ctrl.Antecedent(np.arange(0, 11), 'Intensidade dor artic.')

    # # edema_art = 0
    # edema_art_intd = ctrl.Antecedent(np.arange(0, 11), 'Intensdd. edema')

    # # conjuntivite = ctrl.Antecedent(np.arange(0,2), 'conjuntivite')

    # # dor_cabeca_freq = 0
    # dor_cabeca_intd = ctrl.Antecedent(np.arange(0, 11), 'Intendd. dor cabeça')

    # coceira = ctrl.Antecedent(np.arange(0, 11), 'Intdd coceira')

    # hiptrof_gangli_freq = 0
    # disc_hemo = 0
    # acomet_neuro = 0

    ################################################

    # idade.automf(3)
    febre.automf(3)
    # dias_febre.automf(3)
    dias_febre['curta'] = fuzz.trimf(dias_febre.universe, [0, 0, 3])
    dias_febre['media'] = fuzz.trimf(dias_febre.universe, [2, 3, 5])
    dias_febre['longa'] = fuzz.trimf(dias_febre.universe, [4, 7, 7])
    # dias_febre.view()
    # input("a")

    # # mancha.automf(3) 0
    # mancha_freq.automf(3)

    dor_musc_freq.automf(3)

    # dor_art_freq.automf(3)
    # dor_art_intensidade.automf(3)

    # # edema_art.automf(3)
    # edema_art_intd.automf(3)
    # # conjuntivite.automf(3)
    # # dor_cabeca_freq.automf(3)
    # dor_cabeca_intd.automf(3)
    # coceira.automf(3)
    # # hiptrof_gangli_freq.automf(3)
    # # disc_hemo.automf(3)
    # # acomet_neuro.automf(3)

    ################################################
    dengue = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'dengue')
    dengue['baixa'] = fuzz.trimf(dengue.universe, [0, 0, 0.4])
    dengue['media'] = fuzz.trimf(dengue.universe, [0.3, 0.5, 1.0])
    dengue['alta'] = fuzz.trimf(dengue.universe, [0.5, 1.0, 1.0])
    ################################################
    zika = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'zika')
    zika['baixa'] = fuzz.trimf(dengue.universe, [0, 0, 0.4])
    zika['media'] = fuzz.trimf(dengue.universe, [0.3, 0.5, 1.0])
    zika['alta'] = fuzz.trimf(dengue.universe, [0.5, 1.0, 1.0])
    ################################################
    chikungunya = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'chikungunya')
    chikungunya['baixa'] = fuzz.trimf(dengue.universe, [0, 0, 0.4])
    chikungunya['media'] = fuzz.trimf(dengue.universe, [0.3, 0.5, 1.0])
    chikungunya['alta'] = fuzz.trimf(dengue.universe, [0.5, 1.0, 1.0])
    ################################################

    rule1 = ctrl.Rule(febre['good'] & dias_febre['longa'], consequent=(dengue['alta'], zika['baixa'], chikungunya['baixa']))
    rule11 = ctrl.Rule(febre['good'] & dias_febre['media'], consequent = (dengue['alta'], zika['baixa'], chikungunya['alta']))
    rule111 = ctrl.Rule(febre['good'] & dias_febre['curta'], consequent = (dengue['baixa'], zika['baixa'], chikungunya['alta']))

    rule2 = ctrl.Rule(febre['poor'] | dias_febre['curta'], consequent = (dengue['baixa'], zika['alta'], chikungunya['baixa'] ))
    rule22 = ctrl.Rule(febre['poor'] & dias_febre['media'], consequent = (dengue['baixa'], zika['alta'], chikungunya['baixa']))
    rule222 = ctrl.Rule(febre['poor'] & dias_febre['longa'], consequent = (dengue['baixa'], zika['media'], chikungunya['baixa']))

    rule3 = ctrl.Rule(febre['average'] & dias_febre['longa'], consequent = (dengue['alta'], zika['media'], chikungunya['baixa']))
    rule33 = ctrl.Rule(febre['average'] & dias_febre['media'], consequent = (dengue['media'], zika['media'], chikungunya['baixa']))
    rule333 = ctrl.Rule(febre['average'] & dias_febre['curta'], consequent = (dengue['baixa'], zika['alta'], chikungunya['baixa']))

    # rule_dm = ctrl.Rule(dor_musc_freq['good'])

    diag_ctrl = ctrl.ControlSystem([rule1, rule11, rule111, rule2, rule22, rule222,
                                     rule3, rule33, rule333])
    diag_result = ctrl.ControlSystemSimulation(diag_ctrl)

    diag_result.input['febre'] = p1.temp_corpo
    diag_result.input['dias_febre'] = p1.dias_febre

    diag_result.compute()

    print("dengue = ", round(diag_result.output['dengue'], 2) )
    print("zika = ", round(diag_result.output['zika'],2) )
    print("chico = ", round(diag_result.output['chikungunya'],2) )

    # dengue.view(sim=diag_result)
    # zika.view(sim=diag_result)
    # chikungunya.view(sim=diag_result)
    # input("Enter")

main()