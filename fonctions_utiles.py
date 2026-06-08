import numpy as np

def calculer_revenu_net (revenu_brut) :
    abbatement_forfaitaire = 0.9
    revenu_net = revenu_brut*abbatement_forfaitaire
    return revenu_net

def calculer_revenu_imposable (revenu_net, parts) :
    revenu_imposable = revenu_net / parts
    return revenu_imposable

def formule_ir(revenu_net):
    impot = 0

    P0 = 0
    P1 = 0.11
    P2 = 0.30
    P3 = 0.41
    P4 = 0.45

    T1 = 11600
    T2 = 29579
    T3 = 84577
    T4 = 181917

    impot += np.where(revenu_net > T1, P1 * (np.minimum(revenu_net, T2) - T1), 0)
    impot += np.where(revenu_net > T2, P2 * (np.minimum(revenu_net, T3) - T2), 0)
    impot += np.where(revenu_net > T3, P3 * (np.minimum(revenu_net, T4) - T3), 0)
    impot += np.where(revenu_net > T4, P4 * (revenu_net - T4), 0)

    return impot

def calcul_droits_simples(impots_par_parts, parts) :
    droits_simples = impots_par_parts * parts
    return droits_simples

def calcul_decote(impot_brut):
    decote = 897 - (0.4525 * impot_brut)
    # La décote ne peut pas être négative
    decote = np.maximum(0, decote)
    return decote

def enleve_decote(impot_brut, decote) :
    impot = np.maximum(0,impot_brut - decote)
    return impot