def calcul_decote(impot_brut, nb_parts):
    if nb_parts <= 1:  
        decote = 897 - (0.4525 * impot_brut)
    else:              
        decote = 1483 - (0.4525 * impot_brut)
    # La décote ne peut pas être négative
    decote = max(0, decote)
    return decote