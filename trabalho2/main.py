import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt
import matplotlib


###########
from Pac import *
###########

def main():

    p1 = Paciente()
    p1 = getStatusPaciente(p1)

    #########

    febre = ctrl.Antecedent(np.arange(36, 40.5, 0.5), 'febre')
    dias_febre = ctrl.Antecedent(np.arange(0, 8, 1), 'dias_febre')

    #########

    # manchas = 
    # mancha_freq = ctrl.Antecedent(np.arange(0,8), 'dia aparicao mancha')

    #########

    # dor_musc_freq = ctrl.Antecedent(np.arange(0,11), 'dor_musc_freq')

    #########

    # dor_art_freq = ctrl.Antecedent(np.arange(0, 11), 'Freq. dor artic.')
    # dor_art_intensidade = ctrl.Antecedent(np.arange(0, 11), 'Intensidade dor artic.')

    #########

    edema_art = ctrl.Antecedent(np.arange(0,3), 'edema_art')
    edema_intd = ctrl.Antecedent(np.arange(1, 11), 'edema_intd')

    #########

    conjuntivite = ctrl.Antecedent(np.arange(0,3), 'conjuntivite')

    #########

    # # dor_cabeca_freq = 0
    # dor_cabeca_intd = ctrl.Antecedent(np.arange(0, 11), 'Intendd. dor cabeça')

    #########

    coceira = ctrl.Antecedent(np.arange(0, 11), 'coceira')

    #########

    # hiptrof_gangli_freq = ctrl.Antecedent(np.arange(0,2), 'ganglionar')

    #########

    disc_hemo = ctrl.Antecedent(np.arange(0,3), 'disc_hemo')

    #########

    acomet_neuro = ctrl.Antecedent(np.arange(0,3), 'acomet_neuro')
    neonato = ctrl.Antecedent(np.arange(0,3), 'neonato')

    ############################################### OKOKOKOK
    febre.automf(3)

    dias_febre['curta'] = fuzz.trimf(dias_febre.universe, [0, 0, 3])
    dias_febre['media'] = fuzz.trimf(dias_febre.universe, [2, 3, 5])
    dias_febre['longa'] = fuzz.trimf(dias_febre.universe, [4, 7, 7])

    ############################################### 

    # # mancha.automf(3) 0
    # mancha_freq.automf(3)

    ###############################################

    # dor_musc_freq.automf(3)

    ###############################################

    # dor_art_freq.automf(3)
    # dor_art_intensidade.automf(3)

    ############################################### OKOKOKOK

    edema_art['nao'] = fuzz.trimf(edema_art.universe, [0,0,1])
    edema_art['sim'] = fuzz.trimf(edema_art.universe, [1,2,2])

    edema_intd.automf(3)

    ###############################################

    # # dor_cabeca_freq.automf(3)
    # dor_cabeca_intd.automf(3)

    ###############################################

    # hiptrof_gangli_freq)

    ############################################### OKOKOKOK

    coceira.automf(3)

    ###############################################

    acomet_neuro['nao'] = fuzz.trimf(disc_hemo.universe, [0,0,1])
    acomet_neuro['sim'] = fuzz.trimf(disc_hemo.universe, [1,2,2])

    neonato['nao'] = fuzz.trimf(conjuntivite.universe, [0,0,1])
    neonato['sim'] = fuzz.trimf(conjuntivite.universe, [1,2,2])

    ############################################### OKOKOKOK

    conjuntivite['nao'] = fuzz.trimf(conjuntivite.universe, [0,0,1])
    conjuntivite['sim'] = fuzz.trimf(conjuntivite.universe, [1,2,2])

    ############################################### OKOKOK

    disc_hemo['nao'] = fuzz.trimf(disc_hemo.universe, [0,0,1])
    disc_hemo['sim'] = fuzz.trimf(disc_hemo.universe, [1,2,2])

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
    
    ###############################################

    rule_edema1 = ctrl.Rule(edema_art['nao'], consequent=(dengue['alta'], zika['baixa'], chikungunya['baixa']))
    rule_edema2 = ctrl.Rule(edema_art['sim'], consequent=(dengue['baixa'], zika['alta'], chikungunya['alta']))

    rule_edema3 = ctrl.Rule(edema_intd['good'], consequent=(zika['baixa'], chikungunya['alta']))
    rule_edema4 = ctrl.Rule(edema_intd['average'], consequent=(zika['alta'], chikungunya['alta']))
    rule_edema5 = ctrl.Rule(edema_intd['poor'], consequent=(zika['alta'], chikungunya['media']))

    ###############################################

    rule_coceira = ctrl.Rule(coceira['average'] | coceira['good'], consequent=(zika['alta'], dengue['baixa'], chikungunya['baixa']))
    rule_coceira2 = ctrl.Rule(coceira['poor'], consequent=(zika['baixa'], dengue['alta'], chikungunya['alta']))

    ###############################################

    rule_conjuntivite = ctrl.Rule(conjuntivite['sim'], consequent=(zika['alta'], chikungunya['media'], dengue['baixa']))

    ###############################################

    rule_hemo = ctrl.Rule(disc_hemo['sim'], consequent=(zika['baixa'], dengue['media'], chikungunya['baixa']))

    ###############################################

    rule_neuro1 = ctrl.Rule(acomet_neuro['sim'], consequent=(dengue['baixa'], zika['media'], chikungunya['baixa']))
    # rule_neuro2 = ctrl.Rule(acomet_neuro['sim'] , consequent=(dengue['baixa'], zika['media'], chikungunya['baixa']))

    ###############################################

    # rule_dm = ctrl.Rule(dor_musc_freq['good'])


    diag_ctrl = ctrl.ControlSystem([rule1, rule11, rule111, rule2, rule22, rule222,
                                    rule3, rule33, rule333,
                                    rule_edema1, rule_edema2, rule_edema3, rule_edema4, rule_edema5,
                                    rule_coceira, rule_coceira2,
                                    rule_hemo, rule_conjuntivite])

    diag_result = ctrl.ControlSystemSimulation(diag_ctrl)

    diag_result.input['febre'] = p1.temp_corpo
    diag_result.input['dias_febre'] = p1.dias_febre
    
    diag_result.input['edema_art'] = p1.edema_art
    diag_result.input['edema_intd'] = p1.edema_intd


    diag_result.input['coceira'] = p1.coceira

    diag_result.input['disc_hemo'] = p1.disc_hemo

    diag_result.input['conjuntivite'] = p1.conjuntivite



    diag_result.compute()

    print("dengue = ", round(diag_result.output['dengue'], 2) )
    print("zika = ", round(diag_result.output['zika'],2) )
    print("chico = ", round(diag_result.output['chikungunya'],2) )

    # dengue.view(sim=diag_result)
    # zika.view(sim=diag_result)
    # chikungunya.view(sim=diag_result)
    # input("Enter")

main()