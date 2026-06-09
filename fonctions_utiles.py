import numpy as np
from parameters import *

def calculer_revenu_net (revenu_brut) :
    revenu_net = revenu_brut*ABATTEMENT_FORFAITAIRE
    return revenu_net

def quotient_familial (revenu_net, nb_parts):
    revenu_imposable = revenu_net/nb_parts
    return revenu_imposable

def formule_ir(revenu_net):
    impot = 0

    impot += np.where(revenu_net > T1, P1 * (np.minimum(revenu_net, T2) - T1), 0)
    impot += np.where(revenu_net > T2, P2 * (np.minimum(revenu_net, T3) - T2), 0)
    impot += np.where(revenu_net > T3, P3 * (np.minimum(revenu_net, T4) - T3), 0)
    impot += np.where(revenu_net > T4, P4 * (revenu_net - T4), 0)

    return impot

def calcul_decote(impot_brut):
    decote = SEUIL_DECOTE_SEUL - (TAUX_DECOTE * impot_brut)
    # La décote ne peut pas être négative
    decote = np.maximum(0, decote)
    return decote

def enleve_decote(impot_brut, decote) :
    impot = np.maximum(0,impot_brut - decote)
    return impot

def calcul_taux_imposition(impot,revenu_brut) :
    taux_imposition = impot/revenu_brut
    return taux_imposition
