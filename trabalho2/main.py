import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

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
    mancha = ctrl.Antecedent(np.arange(0,3), 'mancha')
    dia_mancha = ctrl.Antecedent(np.arange(0,8), 'dia_mancha')

    #########

    dor_musc_freq = ctrl.Antecedent(np.arange(0,11), 'dor_musc_freq')

    #########

    dor_art_freq = ctrl.Antecedent(np.arange(0, 11), 'art_freq')
    dor_art_intensidade = ctrl.Antecedent(np.arange(0, 11), 'art_intd')

    #########

    edema_art = ctrl.Antecedent(np.arange(0,3), 'edema_art')
    edema_intd = ctrl.Antecedent(np.arange(1, 11), 'edema_intd')

    #########

    conjuntivite = ctrl.Antecedent(np.arange(0,3), 'conjuntivite')

    #########

    dor_cabeca_freq = ctrl.Antecedent(np.arange(0,11), 'dor_cabeca_freq')
    dor_cabeca_intd = ctrl.Antecedent(np.arange(0, 11), 'dor_cabeca_intd')

    #########

    coceira = ctrl.Antecedent(np.arange(0, 11), 'coceira')

    #########

    hiptrof_gangli_freq = ctrl.Antecedent(np.arange(1,11), 'ganglionar')

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

    mancha['nao'] = fuzz.trimf(mancha.universe, [0,0,1])
    mancha['sim'] = fuzz.trimf(mancha.universe, [1,2,2])

    dia_mancha['cedo'] = fuzz.trimf(dia_mancha.universe, [0, 0, 3])
    dia_mancha['normal'] = fuzz.trimf(dia_mancha.universe, [2, 3, 5])
    dia_mancha['tarde'] = fuzz.trimf(dia_mancha.universe, [4, 7, 7])

    ###############################################

    dor_musc_freq.automf(3)

    ###############################################

    dor_art_freq.automf(3)
    dor_art_intensidade.automf(3)

    ############################################### OKOKOKOK

    edema_art['nao'] = fuzz.trimf(edema_art.universe, [0,0,1])
    edema_art['sim'] = fuzz.trimf(edema_art.universe, [1,2,2])

    edema_intd.automf(3)

    ###############################################

    dor_cabeca_freq.automf(3)
    dor_cabeca_intd.automf(3)

    ############################################### okokok

    hiptrof_gangli_freq.automf(3)

    ############################################### OKOKOKOK

    coceira.automf(3)

    ############################################### OKOKOK

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
    saudavel = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'saudavel')
    saudavel['baixa'] = fuzz.trimf(dengue.universe, [0, 0, 0.4])
    saudavel['media'] = fuzz.trimf(dengue.universe, [0.3, 0.5, 1.0])
    saudavel['alta'] = fuzz.trimf(dengue.universe, [0.5, 1.0, 1.0])
    ################################################

    rule1 = ctrl.Rule(febre['good'] & dias_febre['longa'], consequent=(dengue['alta'], zika['baixa'], chikungunya['baixa']))
    rule11 = ctrl.Rule(febre['good'] & dias_febre['media'], consequent = (dengue['alta'], zika['baixa'], chikungunya['alta']))
    rule111 = ctrl.Rule(febre['good'] & dias_febre['curta'], consequent = (dengue['baixa'], zika['baixa'], chikungunya['alta']))

    rule2 = ctrl.Rule(febre['poor'] | dias_febre['curta'], consequent = (dengue['baixa'], zika['alta'], chikungunya['baixa'] ))

    rule3 = ctrl.Rule(febre['average'] & dias_febre['longa'], consequent = (dengue['alta'], zika['media'], chikungunya['baixa']))
    rule33 = ctrl.Rule(febre['average'] & dias_febre['media'], consequent = (dengue['media'], zika['media'], chikungunya['baixa']))
    rule333 = ctrl.Rule(febre['average'] & dias_febre['curta'], consequent = (dengue['baixa'], zika['alta'], chikungunya['baixa']))
    
    # ###############################################

    rule_manchas1 = ctrl.Rule(mancha['nao'], zika['baixa'])
    rule_manchas2 = ctrl.Rule(mancha['sim'] | dia_mancha['cedo'], consequent=(dengue['baixa'], zika['alta'], chikungunya['media']))
    rule_manchas3 = ctrl.Rule(mancha['sim'] | dia_mancha['normal'], consequent=(dengue['media'], zika['media'], chikungunya['media']))
    rule_manchas4 = ctrl.Rule(mancha['sim'] | dia_mancha['tarde'], consequent=(dengue['alta'], zika['baixa'], chikungunya['media']))

    # ###############################################

    rule_musc1 = ctrl.Rule(dor_musc_freq['good'], consequent=(dengue['alta'], zika['media'], chikungunya['baixa']))
    rule_musc2 = ctrl.Rule(dor_musc_freq['average'], consequent=(dengue['media'], zika['alta'], chikungunya['media']))
    rule_musc3 = ctrl.Rule(dor_musc_freq['poor'], consequent=(dengue['baixa'], zika['media'], chikungunya['alta']))

    # ###############################################

    rule_art1 = ctrl.Rule(dor_art_intensidade['good'], consequent=(dengue['baixa'], zika['baixa'], chikungunya['alta']))
    rule_art2 = ctrl.Rule(dor_art_intensidade['average'], consequent=(dengue['baixa'], zika['alta'], chikungunya['alta']))
    rule_art3 = ctrl.Rule(dor_art_intensidade['poor'], consequent=(dengue['alta'], zika['alta'], chikungunya['baixa']))

    rule_art4 = ctrl.Rule(dor_art_freq['good'], consequent=(dengue['baixa'], zika['baixa'], chikungunya['alta']))
    rule_art5 = ctrl.Rule(dor_art_freq['average'], consequent=(dengue['baixa'], zika['alta'], chikungunya['baixa']))
    rule_art6 = ctrl.Rule(dor_art_freq['poor'], consequent=(dengue['alta'], zika['media'], chikungunya['baixa']))

    # ###############################################

    rule_edema1 = ctrl.Rule(edema_art['nao'], consequent=(dengue['alta'], zika['baixa'], chikungunya['baixa']))
    rule_edema2 = ctrl.Rule(edema_art['sim'], consequent=(dengue['baixa'], zika['alta'], chikungunya['alta']))

    rule_edema3 = ctrl.Rule(edema_intd['good'], consequent=(zika['baixa'], chikungunya['alta']))
    rule_edema4 = ctrl.Rule(edema_intd['average'], consequent=(zika['alta'], chikungunya['alta']))
    rule_edema5 = ctrl.Rule(edema_intd['poor'], consequent=(zika['alta'], chikungunya['media']))

    # ###############################################

    rule_conjuntivite1 = ctrl.Rule(conjuntivite['sim'], consequent=(dengue['baixa'], zika['alta'], chikungunya['media']))
    # rule_conjuntivite2 = ctrl.Rule(conjuntivite['nao'], consequent=(zika['baixa']))

    # ###############################################

    rule_cabeca1 = ctrl.Rule(dor_cabeca_freq['good'] & dor_cabeca_intd['good'], consequent=(dengue['alta'], zika['media'], chikungunya['baixa']))
    rule_cabeca2 = ctrl.Rule(dor_cabeca_freq['average'] | dor_cabeca_intd['average'], consequent=(dengue['media'], zika['alta'], chikungunya['alta']))
    rule_cabeca3 = ctrl.Rule(dor_cabeca_freq['poor'] | dor_cabeca_intd['poor'], consequent=(dengue['media'], zika['alta'], chikungunya['alta']))

    # ###############################################

    rule_coceira = ctrl.Rule(coceira['average'] | coceira['good'], consequent=(zika['alta'], dengue['baixa'], chikungunya['baixa']))
    rule_coceira2 = ctrl.Rule(coceira['poor'], consequent=(zika['baixa'], dengue['alta'], chikungunya['alta']))

    # ###############################################

    rule_gangli1 = ctrl.Rule(hiptrof_gangli_freq['good'], consequent=(dengue['baixa'], zika['alta'], chikungunya['media']))
    rule_gangli2 = ctrl.Rule(hiptrof_gangli_freq['average'], consequent=(dengue['media'], zika['media'], chikungunya['alta']))
    rule_gangli3 = ctrl.Rule(hiptrof_gangli_freq['poor'], consequent=(dengue['alta'], zika['baixa'], chikungunya['media']))

    # ###############################################

    rule_hemo = ctrl.Rule(disc_hemo['sim'], consequent=(zika['baixa'], dengue['media'], chikungunya['baixa']))

    # ###############################################

    rule_neuro1 = ctrl.Rule(acomet_neuro['sim'], consequent=(dengue['baixa'], zika['media'], chikungunya['baixa']))
    # # rule_neuro2 = ctrl.Rule(acomet_neuro['sim'] , consequent=(dengue['baixa'], zika['media'], chikungunya['baixa']))

    # ###############################################

    diag_ctrl = ctrl.ControlSystem([rule1, rule11, rule111, rule2, rule3, rule33, rule333,
                                    rule_manchas1, rule_manchas2, rule_manchas3, rule_manchas4,
                                    rule_musc1, rule_musc2, rule_musc3, 
                                    rule_art1, rule_art2, rule_art3, rule_art4, rule_art5, rule_art6,
                                    rule_edema1, rule_edema2, rule_edema3, rule_edema4, rule_edema5,
                                    rule_cabeca1, rule_cabeca2, rule_cabeca3,
                                    rule_gangli1, rule_gangli2, rule_gangli3,
                                    rule_coceira, rule_coceira2,
                                    rule_hemo, rule_conjuntivite1, rule_neuro1])


    diag_result = ctrl.ControlSystemSimulation(diag_ctrl)

    ###############################################

    diag_result.input['febre'] = p1.temp_corpo
    diag_result.input['dias_febre'] = p1.dias_febre
    
    diag_result.input['mancha'] = p1.mancha
    diag_result.input['dia_mancha'] = p1.dia_mancha

    diag_result.input['dor_musc_freq'] = p1.dor_musc_freq

    diag_result.input['art_freq'] = p1.dor_art_freq
    diag_result.input['art_intd'] = p1.dor_art_intensidade 

    diag_result.input['edema_art'] = p1.edema_art
    diag_result.input['edema_intd'] = p1.edema_intd

    diag_result.input['conjuntivite'] = p1.conjuntivite

    diag_result.input['dor_cabeca_freq'] = p1.dor_cabeca_freq
    diag_result.input['dor_cabeca_intd'] = p1.dor_cabeca_intd

    diag_result.input['coceira'] = p1.coceira

    diag_result.input['ganglionar'] = p1.hiptrof_gangli_freq

    diag_result.input['disc_hemo'] = p1.disc_hemo

    diag_result.input['acomet_neuro'] = p1.acomet_neuro

    diag_result.compute()

    ###############################################

    print("dengue = ", round(diag_result.output['dengue'], 2) )
    print("zika = ", round(diag_result.output['zika'],2) )
    print("chico = ", round(diag_result.output['chikungunya'],2) )

    # dengue.view(sim=diag_result)
    # zika.view(sim=diag_result)
    # chikungunya.view(sim=diag_result)
    # input("Enter")

##############################################################################################3
##############################################################################################3
##############################################################################################3
##############################################################################################3

    rule_sintozika = ctrl.Rule(antecedent=(hiptrof_gangli_freq['good'] & dia_mancha['cedo']), consequent=(zika['alta'], dengue['baixa'], chikungunya['baixa']))
    rule_sintozika2 = ctrl.Rule(hiptrof_gangli_freq['average'], consequent=(zika['media'], dengue['media'], chikungunya['alta']))
    rule_sintozika3 = ctrl.Rule(hiptrof_gangli_freq['poor'], consequent=(zika['baixa'], dengue['baixa'], chikungunya['baixa']))

    diag_ctrl2 = ctrl.ControlSystem([rule_sintozika ,rule_sintozika2, rule_sintozika3])

    diag_result2 = ctrl.ControlSystemSimulation(diag_ctrl2)

    diag_result2.input['ganglionar'] = p1.hiptrof_gangli_freq
    diag_result2.input['dia_mancha'] = p1.dia_mancha

    diag_result2.compute()

    print("dengue = ", round(diag_result2.output['dengue'], 2) )
    print("zika = ", round(diag_result2.output['zika'],2) )
    print("chico = ", round(diag_result2.output['chikungunya'],2) )




main()