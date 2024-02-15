#!/bin/bash

url="https://www.openml.org/data/download/21756251/dataset"
fichier="dataset_"
dossier="data"

if [ ! -d "$dossier" ]; then

    mkdir -p "$dossier"
    echo "Dossier créé : $dossier"
else
    echo "Le dossier existe déjà : $dossier"
fi

curl $url > "$dossier/$fichier"

echo "Téléchargement terminé. Le fichier est enregistré au répertoire : $dossier au nom $fichier "
