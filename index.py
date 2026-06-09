import numpy as np
from fonctions_utiles import *

def calcul_ir(revenu_brut, adultes, enfants) : #on part du principe qu'on a une seule part
    parts = calcul_parts(adultes, enfants)
    revenu_net = calculer_revenu_net(revenu_brut)
    revenu_imposable = quotient_familial(revenu_net, parts)
    impot_par_parts = formule_ir(revenu_imposable)
    droits_simples = calcul_droits_simples (impot_par_parts, parts)
    decote = calcul_decote(droits_simples)
    impot = enleve_decote(droits_simples, decote)
    impot_final = appliquer_minimum(impot)
    return(impot_final)

revenu_brut = np.array([19500, 20000, 19800])
adultes = np.array([1, 1, 1])
enfants = np.array([0, 0, 0])

impot = np.array(calcul_ir(revenu_brut, adultes, enfants))
print("impot sur le revenu =", impot)

taux_imposition = np.array(calcul_taux_imposition(impot,revenu_brut))
print("taux d'imposition =", np.round(taux_imposition * 100, 1), "%")  #en %
