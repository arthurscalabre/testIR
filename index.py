import numpy as np
from fonctions_utiles import *

def calcul_ir(revenu_brut) : #on part du principe qu'on a une seule part
    revenu_net = calculer_revenu_net(revenu_brut)
    impot_brut = formule_ir(revenu_net)
    decote = calcul_decote(impot_brut)
    impot = enleve_decote(impot_brut, decote)
    return(impot)

revenu_brut = np.array([20000, 70000, 120000])
calcul_ir_vect = np.vectorize(calcul_ir)
print (calcul_ir_vect(revenu_brut))
