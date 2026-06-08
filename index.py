from formule_ir import *
from calculer_revenu_net import *
from calculs_parts import *


revenu_brut = float(input("Entrez votre revenu : "))
revenu_net = calculer_revenu_net(revenu_brut)
revenu_imposable = revenu_net/calcul_parts()
impot_base = formule_ir(revenu_net) * calcul_parts

print("impot sur le revenu =", impot_base)