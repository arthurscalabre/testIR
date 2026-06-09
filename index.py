import numpy as np
from fonctions_utiles import *

def calcul_ir(revenu_brut) : #on part du principe qu'on a une seule part
    revenu_net = np.array(calculer_revenu_net(revenu_brut))
    revenu_imposable = np.array(quotient_familial(revenu_net, parts))
    impot_par_parts = np.array(formule_ir(revenu_imposable))
    droits_simples = np.array(calcul_droits_simples (impot_par_parts, parts))
    decote = np.array(calcul_decote(droits_simples))
    impot = np.array(enleve_decote(droits_simples, decote))
    return(impot)

revenu_brut = np.array([20000, 70000, 120000])
parts = np.array([1, 1, 2])
print (calcul_ir(revenu_brut))
