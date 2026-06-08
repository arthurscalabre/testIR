from calculs_parts import *
from formule_ir import *
from calculer_revenu_net import *
from calcul_decote import *

revenu_brut = float(input("Entrez votre revenu : "))
revenu_net = calculer_revenu_net(revenu_brut)
nb_parts = calcul_parts()
revenu_imposable = revenu_net/nb_parts
impot_brut = formule_ir(revenu_net) * nb_parts
decote = calcul_decote(impot_brut, nb_parts)
impot = impot_brut - decote
print("impot sur le revenu =", impot)