def calcul_parts() : 
    adulte = int(input("Combien d'adultes êtes-vous ? :"))
    enfant = int(input("Combien d'enfants êtes-vous ? :"))
    if enfant<=2 :
        nb_parts = adulte + enfant*0.5
    else :
        nb_parts = adulte + enfant-1 #le -1 correspond au fait que les 2 premiers enfants compte uniquement pour 1part
    return nb_parts