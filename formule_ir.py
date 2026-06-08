def formule_ir(revenu_net):
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

