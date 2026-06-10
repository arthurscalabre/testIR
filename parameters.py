# Taux de la déduction pour frais professionnels :
ABATTEMENT_FORFAITAIRE = 0.9


# Barème de l'impôt sur le revenu

    # Tranches
TRANCHES_IR = (11600, 29579, 84577, 181917)
T1, T2, T3, T4 = TRANCHES_IR
   
    # Taux
TAUX_IR = (0.11, 0.30, 0.41, 0.45)
P1, P2, P3, P4 = TAUX_IR


# Décote
SEUIL_DECOTE_SEUL = 897
SEUIL_DECOTE_COUPLE = 1483
TAUX_DECOTE = 0.4525


# Quotient familial et parts supplémentaires
NB_PARTS_ADULTE = 1
NB_PARTS_ENFANTS_1ou2 = 0.5
NB_PARTS_ENFANTS3 = 1

PLAFOND_PAR_DEMI_PART = 1807
PLAFOND_PAR_PART = PLAFOND_PAR_DEMI_PART * 2

# Seuil de mise en recouvrement de l'impôt
MONTANT_MINIMUM = 61

