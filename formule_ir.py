def formule_ir(revenu):
    value_type = float
    impot = 0
    
    P0 = 0
    P1 = 0.11
    P2 = 0.30
    P3 = 0.41
    P4 = 0.45

    T1 = 11600
    T2 = 29579
    T3 = 84577
    T4 = 181917

    if revenu > T1:
        if revenu > T2:
            if revenu > T3:
                if revenu > T4:
                    impot += P1 * (T2 - T1)
                    impot += P2 * (T3 - T2)
                    impot += P3 * (T4 - T3)
                    impot += P4 * (revenu - T4)
                else:
                    impot += P1 * (T2 - T1)
                    impot += P2 * (T3 - T2)
                    impot += P3 * (revenu - T3)
            else:
                impot += P1 * (T2 - T1)
                impot += P2 * (revenu - T2)
        else:
            impot = P1 * (revenu - T1)
    else:
        impot = 0

    return impot

#appel de la formule pour test
revenu = float(input("Entrez votre revenu : "))
print("impot sur le revenu =", formule_ir(revenu))
