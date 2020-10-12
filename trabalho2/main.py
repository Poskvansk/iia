import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

###########
from pacienteModule import *
###########

def main():

    p1 = Paciente()
    p1 = getStatusPaciente(p1)

    febre = ctrl.Antecedent(np.arange(36, 40.5, 0.5), 'febre')
    dias_febre = ctrl.Antecedent(np.arange(0, 8, 1), 'dias_febre')

    mancha = ctrl.Antecedent(np.arange(0,3), 'mancha')
    dia_mancha = ctrl.Antecedent(np.arange(0,8), 'dia_mancha')

    dor_musc = ctrl.Antecedent(np.arange(0, 3), 'dor_musc')
    dor_musc_intd = ctrl.Antecedent(np.arange(0,11), 'dor_musc_intd')

    dor_art = ctrl.Antecedent(np.arange(0, 3), 'dor_art')
    dor_art_intensidade = ctrl.Antecedent(np.arange(0, 11), 'art_intd')

    edema_art = ctrl.Antecedent(np.arange(0,3), 'edema_art')
    edema_intd = ctrl.Antecedent(np.arange(1, 11), 'edema_intd')

    conjuntivite = ctrl.Antecedent(np.arange(0,3), 'conjuntivite')

    dor_cabeca_freq = ctrl.Antecedent(np.arange(0,11), 'dor_cabeca_freq')
    dor_cabeca_intd = ctrl.Antecedent(np.arange(0, 11), 'dor_cabeca_intd')

    coceira = ctrl.Antecedent(np.arange(0, 11), 'coceira')

    hiptrf_gangli = ctrl.Antecedent(np.arange(1,11), 'ganglionar')

    disc_hemo = ctrl.Antecedent(np.arange(0,3), 'disc_hemo')

    acomet_neuro = ctrl.Antecedent(np.arange(0,3), 'acomet_neuro')
    neonato = ctrl.Antecedent(np.arange(0,3), 'neonato')

    ################################################
    dengue = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'dengue')
    dengue['baixa'] = fuzz.trimf(dengue.universe, [0, 0, 0.3])
    dengue['media'] = fuzz.trimf(dengue.universe, [0.25, 0.5, 0.75])
    dengue['alta'] = fuzz.trimf(dengue.universe, [0.7, 1.0, 1.0])
    ################################################
    zika = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'zika')
    zika['baixa'] = fuzz.trimf(dengue.universe, [0, 0, 0.3])
    zika['media'] = fuzz.trimf(dengue.universe, [0.25, 0.5, 0.75])
    zika['alta'] = fuzz.trimf(dengue.universe, [0.7, 1.0, 1.0])
    ################################################
    chikungunya = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'chikungunya')
    chikungunya['baixa'] = fuzz.trimf(dengue.universe, [0, 0, 0.3])
    chikungunya['media'] = fuzz.trimf(dengue.universe, [0.25, 0.5, 0.75])
    chikungunya['alta'] = fuzz.trimf(dengue.universe, [0.7, 1.0, 1.0])
    ################################################
    saudavel = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'saudavel')
    saudavel['baixa'] = fuzz.trimf(dengue.universe, [0, 0, 0.3])
    saudavel['media'] = fuzz.trimf(dengue.universe, [0.25, 0.5, 0.75])
    saudavel['alta'] = fuzz.trimf(dengue.universe, [0.7, 1.0, 1.0])
    ###############################################

    febre['baixa'] = fuzz.trimf(febre.universe, [36, 36, 38.5])
    febre['media'] = fuzz.trimf(febre.universe, [38, 39, 40])
    febre['alta'] = fuzz.trimf(febre.universe, [39, 40, 40])

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

    dor_musc['nao'] = fuzz.trimf(edema_art.universe, [0,0,1])
    dor_musc['sim'] = fuzz.trimf(edema_art.universe, [1,2,2])

    dor_musc_intd.automf(3)

    dor_cabeca_freq.automf(3)
    dor_cabeca_intd.automf(3)

    hiptrf_gangli.automf(3)

    coceira.automf(3)

    dor_art['nao'] = fuzz.trimf(edema_art.universe, [0,0,1])
    dor_art['sim'] = fuzz.trimf(edema_art.universe, [1,2,2])
    dor_art_intensidade.automf(3)

    ############################################### OKOKOKOK

    edema_art['nao'] = fuzz.trimf(edema_art.universe, [0,0,1])
    edema_art['sim'] = fuzz.trimf(edema_art.universe, [1,2,2])

    edema_intd.automf(3)

    ############################################### 

    acomet_neuro['nao'] = fuzz.trimf(disc_hemo.universe, [0,0,1])
    acomet_neuro['sim'] = fuzz.trimf(disc_hemo.universe, [1,2,2])

    neonato['nao'] = fuzz.trimf(conjuntivite.universe, [0,0,1])
    neonato['sim'] = fuzz.trimf(conjuntivite.universe, [1,2,2])

    ############################################### 

    conjuntivite['nao'] = fuzz.trimf(conjuntivite.universe, [0,0,1])
    conjuntivite['sim'] = fuzz.trimf(conjuntivite.universe, [1,2,2])

    ###############################################

    disc_hemo['nao'] = fuzz.trimf(disc_hemo.universe, [0,0,1])
    disc_hemo['sim'] = fuzz.trimf(disc_hemo.universe, [1,2,2])

    ################################################ DENGUE

    rule_sintodengue = ctrl.Rule(antecedent=(dor_musc_intd['good'] & febre['alta'] & dor_cabeca_intd['good']),
                                 consequent=(dengue['alta'], zika['baixa'], chikungunya['baixa'], saudavel['baixa']))

    rule_dormsc = ctrl.Rule(~dor_musc_intd['good'], dengue['baixa']%0.8)

    ################################################  ZIKA

    rule_sintozika = ctrl.Rule(antecedent=( (febre['baixa'] & hiptrf_gangli['good'] & (dia_mancha['cedo'] & mancha['sim'])) | (febre['baixa'] & hiptrf_gangli['good'])) ,
                               consequent=(zika['alta'], dengue['baixa'], chikungunya['baixa'], saudavel['baixa']))

    rule_dsc_hemo = ctrl.Rule(disc_hemo['sim'], zika['baixa'])
    
    ################################################ CHICO

    rule_sintochik = ctrl.Rule(febre['alta'] & dor_art_intensidade['good'],
                               consequent=(dengue['baixa'], zika['baixa'], chikungunya['alta'], saudavel['baixa']))
    

    ################################################ SAUD

    rule_saudavel = ctrl.Rule(antecedent=(febre['baixa'] & mancha['nao'] & dor_musc_intd['poor'] & dor_art_intensidade['poor'] & dor_art['nao']
                              & hiptrf_gangli['poor'] & edema_art['nao'] & conjuntivite['nao'] & dor_cabeca_intd['poor'] & coceira['poor']
                              & disc_hemo['nao'] & hiptrf_gangli['poor']),
                              consequent=(dengue['baixa'], zika['baixa'], chikungunya['baixa'], saudavel['alta'] ))

    ################################################ 

    rule_mancha = ctrl.Rule(mancha['nao'], zika['baixa'])
    rule_mancha2 = ctrl.Rule(mancha['sim'], consequent=(dengue['baixa']%0.1, zika['alta']%0.5, chikungunya['baixa']%0.1, saudavel['baixa']%0.8))
    rule_mancha3 = ctrl.Rule(mancha['sim'] & dia_mancha['cedo'], consequent=(dengue['baixa']%0.3, zika['alta']%0.5, chikungunya['baixa']%0.3, saudavel['baixa']%0.8))

    rule_gangli = ctrl.Rule(~hiptrf_gangli['good'], consequent=(zika['baixa']))
    rule_gangli2 = ctrl.Rule(~hiptrf_gangli['poor'], saudavel['baixa'])
 
    rule_febre1 = ctrl.Rule(febre['baixa'], consequent=(dengue['baixa'], zika['alta']%0.5, chikungunya['baixa'], saudavel['alta']%0.5))
    rule_febre2 = ctrl.Rule(febre['alta'] & dias_febre['longa'], consequent=(dengue['alta'], zika['baixa'], chikungunya['media']%.5, saudavel['baixa']))
    rule_febre3 = ctrl.Rule(febre['alta'] & dias_febre['curta'], consequent=(dengue['media'], zika['baixa'], chikungunya['alta'], saudavel['baixa']))

    rule_dor_musc_intd1 = ctrl.Rule(dor_musc_intd['good'], consequent=(dengue['alta'], zika['baixa'], chikungunya['media']%.5, saudavel['baixa']))
    rule_dor_musc_intd2 = ctrl.Rule(dor_musc_intd['average'], consequent=(dengue['baixa'], zika['baixa'], chikungunya['media']%.5, saudavel['baixa']))
    rule_dor_musc_intd3 = ctrl.Rule(dor_musc_intd['poor'] & dor_musc['sim'], consequent=(dengue['alta'], zika['baixa'], chikungunya['media']%.5, saudavel['baixa']))

    rule_coc = ctrl.Rule(coceira['good'] | coceira['average'], zika['alta']%.7)

    rule_conjt = ctrl.Rule(conjuntivite['sim'], consequent=(zika['alta'], chikungunya['media']%.5))
    rule_no_conjt = ctrl.Rule(conjuntivite['nao'], consequent=(zika['baixa']%.9, saudavel['alta']%0.5))

    rule_edm = ctrl.Rule(edema_art['sim'], consequent=(dengue['baixa'], zika['alta'], chikungunya['baixa'], saudavel['baixa']))
    rule_edm2 = ctrl.Rule(edema_intd['good'] | edema_intd['average'], consequent=(dengue['baixa'], zika['baixa'], chikungunya['alta'], saudavel['baixa']))
    rule_edm3 = ctrl.Rule(edema_intd['poor'] & edema_art['sim'], consequent=(dengue['baixa'], zika['alta'], chikungunya['baixa']))
    rule_no_edm = ctrl.Rule(edema_art['nao'], consequent=(zika['baixa'], chikungunya['baixa'], saudavel['alta']%0.5 ) )

    rule_acmt_nr = ctrl.Rule(acomet_neuro['sim'], consequent=(dengue['baixa'], zika['alta']%.5, chikungunya['baixa'], saudavel['baixa']))

    rule_art1 = ctrl.Rule(dor_art_intensidade['good'] ,consequent=(dengue['baixa'], zika['media']%0.5, chikungunya['alta'], saudavel['baixa']))
    rule_art2 = ctrl.Rule(dor_art_intensidade['average'] ,consequent=(dengue['baixa'], zika['alta']%.5, chikungunya['media']))
    rule_art3 = ctrl.Rule(dor_art_intensidade['poor'] & dor_art['sim'] , consequent=(dengue['alta'], zika['media']%0.5, chikungunya['baixa']%0.5))

    diag_ctrl = ctrl.ControlSystem([rule_sintozika, rule_sintodengue, rule_sintochik, rule_saudavel,
                                     rule_febre1, rule_febre2, rule_febre3,
                                     rule_gangli2, rule_mancha2, rule_mancha3,
                                     rule_dor_musc_intd1, rule_dor_musc_intd2, rule_dor_musc_intd3,
                                     rule_mancha, rule_dormsc, rule_coc, rule_gangli, rule_dsc_hemo,
                                     rule_edm, rule_edm2, rule_edm3, rule_no_edm,
                                     rule_art1, rule_art2, rule_art3,
                                     rule_conjt, rule_no_conjt, rule_acmt_nr])

    diag_result = ctrl.ControlSystemSimulation(diag_ctrl)

    diag_result.input['febre'] = p1.temp_corpo
    diag_result.input['dias_febre'] = p1.dias_febre
    
    diag_result.input['mancha'] = p1.mancha
    diag_result.input['dia_mancha'] = p1.dia_mancha

    diag_result.input['dor_musc'] = p1.dor_musc
    diag_result.input['dor_musc_intd'] = p1.dor_musc_intd

    diag_result.input['dor_art'] = p1.dor_art
    diag_result.input['art_intd'] = p1.dor_art_intensidade 
# 
    diag_result.input['edema_art'] = p1.edema_art
    diag_result.input['edema_intd'] = p1.edema_intd
# 
    diag_result.input['conjuntivite'] = p1.conjuntivite

    # diag_result.input['dor_cabeca_freq'] = p1.dor_cabeca_freq
    diag_result.input['dor_cabeca_intd'] = p1.dor_cabeca_intd

    diag_result.input['coceira'] = p1.coceira

    diag_result.input['ganglionar'] = p1.hiptrf_gangli

    diag_result.input['disc_hemo'] = p1.disc_hemo
# 
    diag_result.input['acomet_neuro'] = p1.acomet_neuro

    diag_result.compute()

    output = []
    output.append(('dengue',round(diag_result.output['dengue'],2)))
    output.append(('zika',round(diag_result.output['zika'],2)))
    output.append(('chikungunya',round(diag_result.output['chikungunya'],2)))
    output.append(('saudavel',round(diag_result.output['saudavel'],2)))
    output = sorted(output, key=lambda tup: tup[1], reverse=True )

    for i in range(len(output)):
        if i == 0:
            print("Seu estado de saúde é, provavelmente: ", output[i])
        else:
            print(output[i])
main()