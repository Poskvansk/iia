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
