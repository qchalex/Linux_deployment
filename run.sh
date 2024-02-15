#!/bin/bash

# Lancement du script collect.sh
echo "Lancement du script collect.sh..."
./collect.sh

# Vérification du statut de sortie du script collect.sh
if [ $? -eq 0 ]; then
    echo "Le script collect.sh s'est exécuté avec succès."

    # Lancement du script transform.py
    echo "Lancement du script transform.py..."
    python3 transform.py

    # Vérification du statut de sortie du script transform.py
    if [ $? -eq 0 ]; then
        echo "Le script transform.py s'est exécuté avec succès."

        # Lancement du script main.py
        echo "Lancement du script main.py..."
        python3 main.py

        # Vérification du statut de sortie du script main.py
        if [ $? -eq 0 ]; then
            echo "Le script main.py s'est exécuté avec succès."
        else
            echo "Erreur : Le script main.py a rencontré un problème."
        fi
    else
        echo "Erreur : Le script transform.py a rencontré un problème."
    fi
else
    echo "Erreur : Le script collect.sh a rencontré un problème."
fi
