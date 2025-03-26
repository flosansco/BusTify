# Bienvenue sur le démonstrateur BusTify ! 🚌

### Résumé
Dans le cadre d’une thèse portant sur la démonstration et l’optimisation de la batterie d’un bus électrique, il nous a été demandé de concevoir un simulateur permettant d’effectuer des calculs de manière simple et rapide.

L’objectif principal est d’estimer la consommation énergétique d’un bus électrique à batterie (BEB) en tenant compte de son environnement opérationnel. 
Pour ce faire, nous suivrons les étapes suivantes :

1. Détermination des conditions de fonctionnement : Identification des paramètres influençant la consommation énergétique (topographie, météo, profil du trajet, etc.).
2. Calcul de la consommation énergétique : Évaluation de la consommation de chaque système du bus pour un trajet donné. Les systèmes étants **la chaine de traction, l'HVAC, la bettreie (BTMS) et l'auxiliaire.**
3. Estimation de la taille de la batterie : Déduction de la capacité de batterie nécessaire pour assurer les trajets prévus.
 
Ce simulateur fournira ainsi une aide pour l’optimisation énergétique et l’évaluation des besoins en batterie.

## Version 0

### Python
Dans un premier temps, cette version est une version de test fonctionnelle. 
Le dossier API contient le fichier api_server.py qui sert d'interface entre le frontend et le backend.
Pour lancer le frontend :
1. Lancer un terminal
2. Vérifier le que le $PYTHONPATH contiennent le chemin vers le dossier API/
3. Lancer la commande :
```
uvicorn api_server:app --reload
```
4. Ouvrez le fichier HTML avec l'outil de votre choix (PyCharm ou Navigateur)

--> La simulation est lancée

### JavaScript
Le fichier html contient un JavaScript faisant appel à la **Simulation** python via **SimulationRequest**

### Roadmap
* ~~Structurer le projet et créer les classes~~
* ~~Ajouter le diagramme UML dans la documentation~~
* Faire les calculs sur l'HVAC
* faire l'ihm pour l'hvac
* trouver comment faire les calculs sur l'HVAC