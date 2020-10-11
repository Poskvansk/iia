import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt


# New Antecedent/Consequent objects hold universe variables and membership
# functions
quality = ctrl.Antecedent(np.arange(0, 11, 1), 'quality')
service = ctrl.Antecedent(np.arange(0, 11, 1), 'service')
tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

# Auto-membership function population is possible with .automf(3, 5, or 7)
quality.automf(3)
service.automf(3)

quality.view()

# Custom membership functions can be built interactively with a familiar,
# Pythonic API
tip['low'] = fuzz.trimf(tip.universe, [0, 0, 13])
tip['medium'] = fuzz.trimf(tip.universe, [0, 13, 25])
tip['high'] = fuzz.trimf(tip.universe, [13, 25, 25])

tip.view()
# input("Press Enter to continue...")
# You can see how these look with .view()
quality['average'].view()

rule1 = ctrl.Rule(quality['poor'] | service['poor'], tip['low'])
rule2 = ctrl.Rule(service['average'], tip['medium'])
rule3 = ctrl.Rule(service['good'] | quality['good'], tip['high'])

# rule1.view()

tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

# Pass inputs to the ControlSystem using Antecedent labels with Pythonic API
# Note: if you like passing many inputs all at once, use .inputs(dict_of_data)
tipping.input['quality'] = 0
tipping.input['service'] = 0

# Crunch the numbers
tipping.compute()

print(tipping.output['tip'])
tip.view(sim=tipping)
plt.pause(8)
# input("Press Enter to continue...")




    # diag_ctrl = ctrl.ControlSystem( [rule1, rule2, rule3, rule11, rule111, rule33, rule333,
    #                                 rule_musc1, rule_musc2, rule_musc3,
    #                                 rule_manchas1, rule_manchas2, rule_manchas3, rule_manchas4,
    #                                 rule_art1, rule_art2, rule_art3, rule_art4, rule_art5, rule_art6,
    #                                 rule_coceira, rule_coceira2,
    #                                 rule_edema1, rule_edema2, rule_edema3, rule_edema4, rule_edema5,
    #                                 rule_gangli1, rule_gangli2, rule_gangli3,
    #                                 rule_cabeca1, rule_cabeca2, rule_cabeca3,
    #                                 rule_conjuntivite1, rule_hemo, rule_neuro1] )


        # rule2 = ctrl.Rule(febre['poor'], consequent = (dengue['baixa'], zika['alta'], chikungunya['baixa'], saudavel['alta']))
    # rule22 = ctrl.Rule(febre['poor'] & dias_febre['media'], consequent = (dengue['baixa'], zika['alta'], chikungunya['baixa']))
    # rule222 = ctrl.Rule(febre['poor'] & dias_febre['longa'], consequent = (dengue['baixa'], zika['media'], chikungunya['baixa']))

#     rule1 = ctrl.Rule(febre['good'] & dias_febre['longa'], consequent=(dengue['alta'], zika['baixa'], chikungunya['baixa']))
#     rule11 = ctrl.Rule(febre['good'] & dias_febre['media'], consequent = (dengue['alta'], zika['baixa'], chikungunya['alta']))
#     rule111 = ctrl.Rule(febre['good'] & dias_febre['curta'], consequent = (dengue['baixa'], zika['baixa'], chikungunya['alta']))

#     rule2 = ctrl.Rule(febre['poor'] | dias_febre['curta'], consequent = (dengue['baixa'], zika['alta'], chikungunya['baixa'] ))

#     rule3 = ctrl.Rule(febre['average'] & dias_febre['longa'], consequent = (dengue['alta'], zika['media'], chikungunya['baixa']))
#     rule33 = ctrl.Rule(febre['average'] & dias_febre['media'], consequent = (dengue['media'], zika['media'], chikungunya['baixa']))
#     rule333 = ctrl.Rule(febre['average'] & dias_febre['curta'], consequent = (dengue['baixa'], zika['alta'], chikungunya['baixa']))
    
#     # ###############################################

#     rule_manchas1 = ctrl.Rule(mancha['nao'], zika['baixa'])
#     rule_manchas2 = ctrl.Rule(mancha['sim'] | dia_mancha['cedo'], consequent=(dengue['baixa'], zika['alta'], chikungunya['media']))
#     rule_manchas3 = ctrl.Rule(mancha['sim'] | dia_mancha['normal'], consequent=(dengue['media'], zika['media'], chikungunya['media']))
#     rule_manchas4 = ctrl.Rule(mancha['sim'] | dia_mancha['tarde'], consequent=(dengue['alta'], zika['baixa'], chikungunya['media']))

#     # ###############################################

#     rule_musc1 = ctrl.Rule(dor_musc['good'], consequent=(dengue['alta'], zika['media'], chikungunya['baixa']))
#     rule_musc2 = ctrl.Rule(dor_musc['average'], consequent=(dengue['media'], zika['alta'], chikungunya['media']))
#     rule_musc3 = ctrl.Rule(dor_musc['poor'], consequent=(dengue['baixa'], zika['media'], chikungunya['alta']))

#     # ###############################################

#     rule_art1 = ctrl.Rule(dor_art_intensidade['good'], consequent=(dengue['baixa'], zika['baixa'], chikungunya['alta']))
#     rule_art2 = ctrl.Rule(dor_art_intensidade['average'], consequent=(dengue['baixa'], zika['alta'], chikungunya['alta']))
#     rule_art3 = ctrl.Rule(dor_art_intensidade['poor'], consequent=(dengue['alta'], zika['alta'], chikungunya['baixa']))

#     rule_art4 = ctrl.Rule(dor_art_freq['good'], consequent=(dengue['baixa'], zika['baixa'], chikungunya['alta']))
#     rule_art5 = ctrl.Rule(dor_art_freq['average'], consequent=(dengue['baixa'], zika['alta'], chikungunya['baixa']))
#     rule_art6 = ctrl.Rule(dor_art_freq['poor'], consequent=(dengue['alta'], zika['media'], chikungunya['baixa']))

#     # ###############################################

#     rule_edema1 = ctrl.Rule(edema_art['nao'], consequent=(dengue['alta'], zika['baixa'], chikungunya['baixa']))
#     rule_edema2 = ctrl.Rule(edema_art['sim'], consequent=(dengue['baixa'], zika['alta'], chikungunya['alta']))

#     rule_edema3 = ctrl.Rule(edema_intd['good'], consequent=(zika['baixa'], chikungunya['alta']))
#     rule_edema4 = ctrl.Rule(edema_intd['average'], consequent=(zika['alta'], chikungunya['alta']))
#     rule_edema5 = ctrl.Rule(edema_intd['poor'], consequent=(zika['alta'], chikungunya['media']))

#     # ###############################################

#     rule_conjuntivite1 = ctrl.Rule(conjuntivite['sim'], consequent=(dengue['baixa'], zika['alta'], chikungunya['media']))
#     # rule_conjuntivite2 = ctrl.Rule(conjuntivite['nao'], consequent=(zika['baixa']))

#     # ###############################################

#     rule_cabeca1 = ctrl.Rule(dor_cabeca_freq['good'] & dor_cabeca_intd['good'], consequent=(dengue['alta'], zika['media'], chikungunya['baixa']))
#     rule_cabeca2 = ctrl.Rule(dor_cabeca_freq['average'] | dor_cabeca_intd['average'], consequent=(dengue['media'], zika['alta'], chikungunya['alta']))
#     rule_cabeca3 = ctrl.Rule(dor_cabeca_freq['poor'] | dor_cabeca_intd['poor'], consequent=(dengue['media'], zika['alta'], chikungunya['alta']))

#     # ###############################################

#     rule_coceira = ctrl.Rule(coceira['average'] | coceira['good'], consequent=(zika['alta'], dengue['baixa'], chikungunya['baixa']))
#     rule_coceira2 = ctrl.Rule(coceira['poor'], consequent=(zika['baixa'], dengue['alta'], chikungunya['alta']))

#     # ###############################################

#     rule_gangli1 = ctrl.Rule(hiptrof_gangli_freq['good'], consequent=(dengue['baixa'], zika['alta'], chikungunya['media']))
#     rule_gangli2 = ctrl.Rule(hiptrof_gangli_freq['average'], consequent=(dengue['media'], zika['media'], chikungunya['alta']))
#     rule_gangli3 = ctrl.Rule(hiptrof_gangli_freq['poor'], consequent=(dengue['alta'], zika['baixa'], chikungunya['media']))

#     # ###############################################

#     rule_hemo = ctrl.Rule(disc_hemo['sim'], consequent=(zika['baixa'], dengue['media'], chikungunya['baixa']))

#     # ###############################################

#     rule_neuro1 = ctrl.Rule(acomet_neuro['sim'], consequent=(dengue['baixa'], zika['media'], chikungunya['baixa']))
#     # # rule_neuro2 = ctrl.Rule(acomet_neuro['sim'] , consequent=(dengue['baixa'], zika['media'], chikungunya['baixa']))

#     # ###############################################

#     diag_ctrl = ctrl.ControlSystem([rule1, rule11, rule111, rule2, rule3, rule33, rule333,
#                                     rule_manchas1, rule_manchas2, rule_manchas3, rule_manchas4,
#                                     rule_musc1, rule_musc2, rule_musc3, 
#                                     rule_art1, rule_art2, rule_art3, rule_art4, rule_art5, rule_art6,
#                                     rule_edema1, rule_edema2, rule_edema3, rule_edema4, rule_edema5,
#                                     rule_cabeca1, rule_cabeca2, rule_cabeca3,
#                                     rule_gangli1, rule_gangli2, rule_gangli3,
#                                     rule_coceira, rule_coceira2,
#                                     rule_hemo, rule_conjuntivite1, rule_neuro1])


#     diag_result = ctrl.ControlSystemSimulation(diag_ctrl)

#     ###############################################

#     diag_result.input['febre'] = p1.temp_corpo
#     diag_result.input['dias_febre'] = p1.dias_febre
    
#     diag_result.input['mancha'] = p1.mancha
#     diag_result.input['dia_mancha'] = p1.dia_mancha

#     diag_result.input['dor_musc'] = p1.dor_musc

#     diag_result.input['art_freq'] = p1.dor_art_freq
#     diag_result.input['art_intd'] = p1.dor_art_intensidade 

#     diag_result.input['edema_art'] = p1.edema_art
#     diag_result.input['edema_intd'] = p1.edema_intd

#     diag_result.input['conjuntivite'] = p1.conjuntivite

#     diag_result.input['dor_cabeca_freq'] = p1.dor_cabeca_freq
#     diag_result.input['dor_cabeca_intd'] = p1.dor_cabeca_intd

#     diag_result.input['coceira'] = p1.coceira

#     diag_result.input['ganglionar'] = p1.hiptrof_gangli_freq

#     diag_result.input['disc_hemo'] = p1.disc_hemo

#     diag_result.input['acomet_neuro'] = p1.acomet_neuro

#     diag_result.compute()

#     ###############################################

#     print("dengue = ", round(diag_result.output['dengue'], 2) )
#     print("zika = ", round(diag_result.output['zika'],2) )
#     print("chico = ", round(diag_result.output['chikungunya'],2) )

#     # dengue.view(sim=diag_result)
#     # zika.view(sim=diag_result)
#     # chikungunya.view(sim=diag_result)
#     # input("Enter")

# ##############################################################################################3
# ##############################################################################################3
