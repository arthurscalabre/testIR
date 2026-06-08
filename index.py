from calculs_parts import *
from formule_ir import *
from calculer_revenu_net import *
from calcul_decote import *
from quotient_familial import *
from enleve_decote import *

revenu_brut = float(input("Entrez votre revenu : "))
revenu_net = calculer_revenu_net(revenu_brut)
nb_parts = calcul_parts()
revenu_imposable = quotient_familial(revenu_net, nb_parts)
impot_brut = formule_ir(revenu_net) * nb_parts
decote = calcul_decote(impot_brut, nb_parts)
impot = enleve_decote(impot_brut, decote)
print("impot sur le revenu =", impot)