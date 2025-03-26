import json


class HVAC:
    """
    L'unité HVAC consiste en 2 pompes à chaleur réversibles (PAC), (20 kW chacune)
    un système de circulation d'air (ACS) et
    un système de gestion thermique de la batterie (BTMS)

    La capacité de chauffage maximale requise est de 35 kW

    Enfin, la consommation électrique totale de l'unité HVAC est la somme de la puissance
    nécessaire pour faire fonctionner les deux PAC, ACS et BTMS.

     La quantité d'air frais requise dépend du nombre de passagers à l'intérieur du BEB. Dans
    le modèle, quatre niveaux d'occupation des passagers sont définis dans le contrôleur de l'unité
    HVAC : (1) Très faible : <10 passagers, (2) Faible : <25 passagers, (3) Moyen : <40 passagers,
    (4) Elevé : >40 passagers.

    """
    pac_consumption: float
    acs_consumption: float
    btms_consumption: float  # à coupler avec la batterie ?


    @staticmethod
    def get_pac_consumption():
        pac_consumption = 100  # GW.h
        return pac_consumption

    @staticmethod
    def get_acs_consumption():
        acs_consumption = 200  # GW.h
        return acs_consumption

    @staticmethod
    def get_btms_consumption():
        btms_consumption = 300  # GW.h
        return btms_consumption