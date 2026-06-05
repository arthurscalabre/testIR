from formule_ir import *
from calculer_revenu_net import *


revenu_brut = float(input("Entrez votre revenu : "))
revenu_net = calculer_revenu_net(revenu_brut)
print("impot sur le revenu =", formule_ir(revenu_net))