import numpy as np
from parameters import *

def calcul_parts (adultes, enfants) : 
    parts = np.where (enfants<=2, adultes*NB_PARTS_ADULTE + enfants*NB_PARTS_ENFANTS_1ou2, adultes + enfants*NB_PARTS_ENFANTS3 - 2*NB_PARTS_ENFANTS_1ou2) #moins 1 car les 2 premiers enfants compte pour 1 (0.5 chacun)
    return parts

def calculer_revenu_net (revenu_brut) :
    revenu_net = revenu_brut*ABATTEMENT_FORFAITAIRE
    return revenu_net

def quotient_familial (revenu_net, parts) :
    revenu_imposable = revenu_net / parts
    return revenu_imposable

def formule_ir(revenu_net):
    impot = 0

    impot += np.where(revenu_net > T1, P1 * (np.minimum(revenu_net, T2) - T1), 0)
    impot += np.where(revenu_net > T2, P2 * (np.minimum(revenu_net, T3) - T2), 0)
    impot += np.where(revenu_net > T3, P3 * (np.minimum(revenu_net, T4) - T3), 0)
    impot += np.where(revenu_net > T4, P4 * (revenu_net - T4), 0)

    return impot

def calcul_droits_simples(impots_par_parts, parts) :
    droits_simples = impots_par_parts * parts
    return droits_simples

def calcul_decote(impot_brut):
    decote = SEUIL_DECOTE_SEUL - (TAUX_DECOTE * impot_brut)
    # La décote ne peut pas être négative
    decote = np.maximum(0, decote)
    return decote

def enleve_decote(impot_brut, decote) :
    impot = np.maximum(0,impot_brut - decote)
    return impot

def appliquer_minimum(impot):
    return np.where(impot < MONTANT_MINIMUM, 0, impot)

def calcul_taux_imposition(impot,revenu_brut) :
    taux_imposition = impot/revenu_brut
    return taux_imposition

def calcul_ir_sans_enfants(revenu_brut, adultes, enfants) : #on part du principe qu'on a une seule part
    parts = np.array(calcul_parts(adultes, enfants))
    revenu_net = calculer_revenu_net(revenu_brut)
    revenu_imposable = quotient_familial(revenu_net, parts)
    impot_par_parts = formule_ir(revenu_imposable)
    droits_simples = calcul_droits_simples (impot_par_parts, parts)
    decote = calcul_decote(droits_simples)
    impot = enleve_decote(droits_simples, decote)
    impot_final = appliquer_minimum(impot)
    return(impot_final)

def plafonnement_QF(impot, parts, revenu_brut, adultes) :
    parts_enfants = parts - adultes * NB_PARTS_ADULTE
    plafonnement = PLAFOND_PAR_PART * parts_enfants
    reduction = calcul_ir_sans_enfants(revenu_brut,adultes,0) - impot #calcul_ir(revenu_brut,adultes,0) = calcule ir sans part enfants
    impot_plafonne = calcul_ir_sans_enfants(revenu_brut,adultes,0) - np.minimum(reduction, plafonnement)
    return impot_plafonne

def calcul_ir(revenu_brut, adultes, enfants) : #on part du principe qu'on a une seule part
    parts = np.array(calcul_parts(adultes, enfants))
    revenu_net = calculer_revenu_net(revenu_brut)
    revenu_imposable = quotient_familial(revenu_net, parts)
    impot_par_parts = formule_ir(revenu_imposable)
    droits_simples = calcul_droits_simples (impot_par_parts, parts)
    impot = np.where(enfants > 0, plafonnement_QF(droits_simples, parts, revenu_brut, adultes), droits_simples)
    decote = calcul_decote(impot)
    impot = enleve_decote(impot, decote)
    impot_final = appliquer_minimum(impot)
    return(impot_final)