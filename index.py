from fonctions_utiles import *

revenu_brut = float(input("Entrez votre revenu : "))
revenu_net = calculer_revenu_net(revenu_brut)
nb_parts = calcul_parts()
revenu_imposable = quotient_familial(revenu_net, nb_parts)
impot_brut = formule_ir(revenu_imposable) * nb_parts
decote = calcul_decote(impot_brut, nb_parts)
impot = enleve_decote(impot_brut, decote)

print("impot sur le revenu =", impot)

taux_imposition = calcul_taux_imposition(impot,revenu_brut)
print("taux d'imposition =", round(taux_imposition * 100, 2), "%")  #en %
