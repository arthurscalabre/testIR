import numpy as np
from fonctions_utiles import *

def calcul_ir(revenu_brut) : #on part du principe qu'on a une seule part
    revenu_net = np.array(calculer_revenu_net(revenu_brut))
    impot_brut = np.array(formule_ir(revenu_net))
    decote = np.array(calcul_decote(impot_brut))
    impot = np.floor(np.array(enleve_decote(impot_brut, decote)))
    return(impot)

revenu_brut = np.array([20000, 70000, 120000])
impot = np.array(calcul_ir(revenu_brut))
print("impot sur le revenu =", impot)

taux_imposition = np.array(calcul_taux_imposition(impot,revenu_brut))
print("taux d'imposition =", np.round(taux_imposition * 100, 1), "%")  #en %
