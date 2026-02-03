import sys
import pandas as pd
import numpy as np
import os

def error(msg):
    print("Error:", msg)
    sys.exit(1)

def main():

    if len(sys.argv) != 5:
        error("Usage: python topsis.py <InputFile> <Weights> <Impacts> <OutputFile>")

    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]

    if not os.path.isfile(input_file):
        error("File not found")

    try:
        df = pd.read_csv(input_file)
    except:
        error("Unable to read input file")

    if df.shape[1] < 3:
        error("Input file must contain three or more columns")

    data = df.iloc[:, 1:]
    if not all(data.apply(lambda x: pd.to_numeric(x, errors='coerce')).notnull().all()):
        error("From 2nd to last columns must contain numeric values only")

    weights = weights.split(',')
    impacts = impacts.split(',')

    if len(weights) != len(impacts) or len(weights) != data.shape[1]:
        error("Number of weights, impacts and columns must be same")

    try:
        weights = np.array(weights, dtype=float)
    except:
        error("Weights must be numeric")

    for i in impacts:
        if i not in ['+', '-']:
            error("Impacts must be either + or -")

    normalized_data = data / np.sqrt((data ** 2).sum())

    weighted_data = normalized_data * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':
            ideal_best.append(weighted_data.iloc[:, i].max())
            ideal_worst.append(weighted_data.iloc[:, i].min())
        else:
            ideal_best.append(weighted_data.iloc[:, i].min())
            ideal_worst.append(weighted_data.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    distance_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
    distance_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

    topsis_score = distance_worst / (distance_best + distance_worst)

    df["Topsis Score"] = topsis_score
    df["Rank"] = topsis_score.rank(ascending=False)

    df.to_csv(output_file, index=False)
    print("TOPSIS analysis completed successfully")

if __name__ == "__main__":
    main()
