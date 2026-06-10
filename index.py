import numpy as np
from fonctions_utiles import *

revenu_brut = np.array([25000, 280000, 74436])
adultes = np.array([1, 2, 2])
enfants = np.array([0, 2, 2])

impot = np.array(calcul_ir(revenu_brut, adultes, enfants))
print("impot sur le revenu =", impot)

taux_imposition = np.array(calcul_taux_imposition(impot,revenu_brut))
print("taux d'imposition =", np.round(taux_imposition * 100, 1), "%")  #en %

