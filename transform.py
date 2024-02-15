import pandas as pd
import os


def convert_to_csv(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    columns = []
    data_lines = []
    data_started = False
    for line in lines:
        if line.startswith('@ATTRIBUTE'):
            column_name = line.split()[1]
            columns.append(column_name)
        elif data_started:
            line = line.strip().replace("'", "")
            data_lines.append(line)
        elif line.startswith('@DATA'):
            data_started = True

    df = pd.DataFrame([line.split(',') for line in data_lines], columns=columns)

    output_dir = os.path.dirname(input_file)
    output_file = os.path.join(output_dir, "dataset.csv")
    df.to_csv(output_file, index=False)
    return output_file

if __name__ == "__main__":
    input_file = "data/dataset_"
    csv_file = convert_to_csv(input_file)
    print("Conversion terminée. Le fichier CSV est enregistré sous :", csv_file)
