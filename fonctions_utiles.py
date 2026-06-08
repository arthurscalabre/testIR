from parameters import *

def calculer_revenu_net (revenu_brut) :
    revenu_net = revenu_brut*ABATTEMENT_FORFAITAIRE
    return revenu_net

def calcul_parts() : 
    adulte = int(input("Combien d'adultes êtes-vous ? : "))
    enfant = int(input("Combien d'enfants êtes-vous ? : "))
    if enfant<=2 :
        nb_parts = adulte + enfant*0.5
    else :
        nb_parts = adulte + enfant-1 #le -1 correspond au fait que les 2 premiers enfants compte uniquement pour 1part
    return nb_parts

def quotient_familial (revenu_net, nb_parts):
    revenu_imposable = revenu_net/nb_parts
    return revenu_imposable

def formule_ir(revenu_net):
    impot = 0

    if revenu_net > T1:
        if revenu_net > T2:
            if revenu_net > T3:
                if revenu_net > T4:
                    impot += P1 * (T2 - T1)
                    impot += P2 * (T3 - T2)
                    impot += P3 * (T4 - T3)
                    impot += P4 * (revenu_net - T4)
                else:
                    impot += P1 * (T2 - T1)
                    impot += P2 * (T3 - T2)
                    impot += P3 * (revenu_net - T3)
            else:
                impot += P1 * (T2 - T1)
                impot += P2 * (revenu_net - T2)
        else:
            impot = P1 * (revenu_net - T1)
    else:
        impot = 0

    return impot

def calcul_decote(impot_brut, nb_parts):
    if nb_parts <= 1:  
        decote = SEUIL_DECOTE_SEUL - (TAUX_DECOTE * impot_brut)
    else:              
        decote = SEUIL_DECOTE_COUPLE - (TAUX_DECOTE * impot_brut)
    # La décote ne peut pas être négative
    decote = max(0, decote)
    return decote

def enleve_decote(impot_brut, decote) :
    impot = impot_brut - decote
    return impot