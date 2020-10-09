import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

febre = ctrl.Antecedent(np.arange(37, 40.5, 0.5, dtype=float), 'febre')
dor = ctrl.Antecedent(np.arange(0, 11, 1), 'dor')

dengue = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'dengue')
# zika = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'zika')
# chico = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'chico')

febre.automf(3)
dor.automf(3)

dengue['baixa'] = fuzz.trimf(dengue.universe, [0, 0, 0.4])
dengue['media'] = fuzz.trimf(dengue.universe, [0.3, 0.5, 1.0])
dengue['alta'] = fuzz.trimf(dengue.universe, [0.5, 1.0, 1.0])
# zika.automf(3)
# chico.automf(3)

# febre['low'] = fuzz.trimf(febre.universe, [37, 37, 38.5])
# febre['mid'] = fuzz.trimf(febre.universe, [37, 38.5, 39.5])
# febre['high'] = fuzz.trimf(febre.universe, [38, 40, 40])
# febre.view()
# dengue.view()

rule1 = ctrl.Rule(febre['good'], dengue['alta'])
rule2 = ctrl.Rule(febre['poor'], dengue['baixa'])
rule3 = ctrl.Rule(febre['average'], dengue['media'])

rule4 = ctrl.Rule(dor['good'], dengue['alta'])
rule5 = ctrl.Rule(dor['poor'], dengue['baixa'])
rule6 = ctrl.Rule(dor['average'], dengue['media'])


graus = int(input("Quantos gaus: "))
intensidade = int(input('Nivel dor: '))

# tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
tipping = ctrl.ControlSystemSimulation(tipping_ctrl)

tipping.input['febre'] = graus
tipping.input['dor'] = intensidade

tipping.compute()

print(tipping.output['dengue'])
dengue.view(sim=tipping)
input("Press Enter to continue...")

