import numpy as np
from parameters import *

# ─── 1. FOYER FISCAL ─────────────────────────────────────────────────────────

def calcul_parts (adultes, enfants) : 
    return np.where (enfants<=2, adultes*NB_PARTS_ADULTE + enfants*NB_PARTS_ENFANTS_1ou2, adultes + enfants*NB_PARTS_ENFANTS3 - 2*NB_PARTS_ENFANTS_1ou2) #moins 1 car les 2 premiers enfants compte pour 1 (0.5 chacun)

def calcul_parts_enfants(parts, adultes):
    return parts - adultes * NB_PARTS_ADULTE

# ─── 2. ASSIETTE IMPOSABLE ───────────────────────────────────────────────────

def calculer_revenu_net (revenu_brut) :
    return revenu_brut * (1 - ABATTEMENT_FORFAITAIRE)

def quotient_familial (revenu_net, parts) :
    return revenu_net / parts

# ─── 3. BARÈME PROGRESSIF ────────────────────────────────────────────────────

def formule_ir(revenu_net):
    impot = 0
    impot += np.where(revenu_net > T1, P1 * (np.minimum(revenu_net, T2) - T1), 0)
    impot += np.where(revenu_net > T2, P2 * (np.minimum(revenu_net, T3) - T2), 0)
    impot += np.where(revenu_net > T3, P3 * (np.minimum(revenu_net, T4) - T3), 0)
    impot += np.where(revenu_net > T4, P4 * (revenu_net - T4), 0)
    return impot

def calcul_droits_simples(revenu_brut, adultes, enfants) :
    parts = calcul_parts(adultes, enfants)
    revenu_net = calculer_revenu_net(revenu_brut)
    revenu_qf = quotient_familial(revenu_net, parts)
    return formule_ir(revenu_qf) * parts

# ─── 4. CORRECTIONS ET MÉCANISMES D'ALLÈGEMENT ───────────────────────────────

def plafonnement_QF(droits, parts, revenu_brut, adultes) :
    parts_enfants = calcul_parts_enfants(parts, adultes)
    plafond = PLAFOND_PAR_PART * parts_enfants
    reduction = calcul_droits_simples(revenu_brut,adultes,0) - droits #calcul_ir(revenu_brut,adultes,0) = calcule ir sans part enfants
    return calcul_droits_simples(revenu_brut,adultes,0) - np.minimum(reduction, plafond)

def calcul_decote(impot_brut, adultes):
    seuil = np.where(adultes >= 2, SEUIL_DECOTE_COUPLE, SEUIL_DECOTE_SEUL)
    return np.maximum(0, seuil - TAUX_DECOTE * impot_brut)

def enleve_decote(impot_brut, decote) :
    impot = np.maximum(0,impot_brut - decote)
    return impot

def appliquer_minimum(impot):
    return np.where(impot < MONTANT_MINIMUM, 0, impot)

# ─── 5. CALCUL PRINCIPAL ─────────────────────────────────────────────────────

def calcul_ir(revenu_brut, adultes, enfants):
    parts  = np.array(calcul_parts(adultes, enfants))
    droits = calcul_droits_simples(revenu_brut, adultes, enfants)
    # Plafonnement QF avant décote
    droits = np.where(enfants > 0,plafonnement_QF(droits, parts, revenu_brut, adultes),droits)
    decote = calcul_decote(droits, adultes)
    impot  = enleve_decote(droits, decote)
    return appliquer_minimum(impot)

# ─── 6. ANALYSE ──────────────────────────────────────────────────────────────

def calcul_taux_imposition(impot,revenu_brut) :
    taux_imposition = impot/revenu_brut
    return taux_imposition