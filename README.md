# Bienvenue sur le démonstrateur BusTify ! 🚌

## Version 0

### Python
Dans un premier temps, cette version est une version de test fonctionnelle. 
Le dossier API contient le fichier api_server.py qui sert d'interface entre le frontend et le backend.
Pour lancer le frontend :
1. Lancer un terminal
2. Vérifier le que le $PYTHONPATH contiennent le chemin vers le dossier API/
3. Lance la commande 
```uvicorn api_server:app --reload```
4. Ouvrez le fichier HTML avec l'outil de votre choix (PyCharm ou Navigateur)

--> La simulation est lancée

### JavaScript
Le fichier html contient un JavaScript faisant appel à la **Simulation** python via **SimulationRequest**

### A venir
* Structurer le projet et créer les classes
* Ajouter le diagramme UML dans la documentation