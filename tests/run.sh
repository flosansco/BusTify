#!/bin/bash

# Vérifie si uvicorn est installé
if ! command -v uvicorn &> /dev/null
then
    echo "⚠️  uvicorn n'est pas installé. Installe-le avec : pip install uvicorn"
    exit 1
fi

# Exécute uvicorn avec le module backend
echo "🚀 Démarrage du serveur Uvicorn..."
uvicorn api_server:app --reload
