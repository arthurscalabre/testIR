# ─── ABATTEMENT FORFAITAIRE ──────────────────────────────────────────────────
# Taux d'abattement pour frais professionnels (10%)
ABATTEMENT_FORFAITAIRE = 0.1

# ─── BARÈME DE L'IMPÔT SUR LE REVENU ─────────────────────────────────────────
## Tranches
TRANCHES_IR = (11600, 29579, 84577, 181917)
T1, T2, T3, T4 = TRANCHES_IR
   
## Taux
TAUX_IR = (0.11, 0.30, 0.41, 0.45)
P1, P2, P3, P4 = TAUX_IR


# ─── DÉCOTE ───────────────────────────────────────────────────────────────────
SEUIL_DECOTE_SEUL = 897
SEUIL_DECOTE_COUPLE = 1483
TAUX_DECOTE = 0.4525


# ─── QUOTIENT FAMILIAL ────────────────────────────────────────────────────────
NB_PARTS_ADULTE = 1
NB_PARTS_ENFANTS_1ou2 = 0.5
NB_PARTS_ENFANTS3 = 1

# Plafond de l'avantage fiscal par part entière d'enfant (= 2 × 1 807 €)
PLAFOND_PAR_DEMI_PART = 1807
PLAFOND_PAR_PART = PLAFOND_PAR_DEMI_PART * 2

# ─── SEUIL DE MISE EN RECOUVREMENT ───────────────────────────────────────────
MONTANT_MINIMUM = 61

