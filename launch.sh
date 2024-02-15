#!/bin/bash

echo "Lancement du script collect.sh..."
./collect.sh

if [ $? -eq 0 ]; then
    echo "Le script collect.sh s'est exécuté avec succès."

    echo "Lancement du script transform.py..."
    python3 transform.py

    if [ $? -eq 0 ]; then
        echo "Le script transform.py s'est exécuté avec succès."

        echo "Lancement du script main.py..."
        python3 main.py

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
