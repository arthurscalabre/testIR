from calculs_parts import *
from formule_ir import *
from calculer_revenu_net import *



revenu_brut = float(input("Entrez votre revenu : "))
revenu_net = calculer_revenu_net(revenu_brut)
nb_parts = calcul_parts()
revenu_imposable = revenu_net/nb_parts
impot_base = formule_ir(revenu_net) * nb_parts
print("impot sur le revenu =", impot_base)