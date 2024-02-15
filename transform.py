import pandas as pd
import os

def convert_to_csv(input_file):
    # Lecture du fichier ARFF
    with open(input_file, 'r') as f:
        lines = f.readlines()

    # Récupération des noms de colonnes et des lignes de données
    columns = []
    data_lines = []
    data_started = False
    for line in lines:
        if line.startswith('@ATTRIBUTE'):
            # Utilisation d'une expression régulière plus robuste pour extraire les noms de colonnes
            column_name = line.split()[1]
            columns.append(column_name)
        elif data_started:
            # Supprimer les guillemets des lignes de données
            line = line.strip().replace("'", "")
            data_lines.append(line)
        elif line.startswith('@DATA'):
            data_started = True

    # Création d'un DataFrame pandas
    df = pd.DataFrame([line.split(',') for line in data_lines], columns=columns)

    # Écriture du DataFrame au format CSV
    output_dir = os.path.dirname(input_file)
    output_file = os.path.join(output_dir, "dataset.csv")
    df.to_csv(output_file, index=False)
    return output_file

if __name__ == "__main__":
    input_file = "data/dataset_"
    csv_file = convert_to_csv(input_file)
    print("Conversion terminée. Le fichier CSV est enregistré sous :", csv_file)
