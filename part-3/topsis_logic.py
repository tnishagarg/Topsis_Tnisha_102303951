import pandas as pd
import numpy as np

def run_topsis(input_file, weights_str, impacts_str, output_file):
    df = pd.read_csv(input_file,sep=None, engine='python', encoding='latin1')
    df = df.dropna(axis=1, how='all')
    if df.shape[1] < 3:
        return "Input file must contain at least three columns."

    criteria_data = df.iloc[:, 1:]
    num_criteria = criteria_data.shape[1]
    if not np.all(criteria_data.applymap(np.isreal)):
        return "From 2nd to last columns must contain numeric values only."

    criteria_data = criteria_data.astype(float)

    try:
        weights = list(map(float, weights_str.split(",")))
    except:
        return "Weights must be numeric and comma separated."

    impacts = impacts_str.split(",")

    if len(weights) != num_criteria:
        return f"Error: You provided {len(weights)} weights, but the file has {num_criteria} criteria columns."

    if len(impacts) != num_criteria:
        return f"Error: You provided {len(impacts)} impacts, but the file has {num_criteria} criteria columns."

    for impact in impacts:
        if impact not in ["+", "-"]:
            return "Impacts must be '+' or '-' only."

    norm_data = criteria_data / np.sqrt((criteria_data ** 2).sum())
    weighted_data = norm_data * weights

    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == "+":
            ideal_best.append(weighted_data.iloc[:, i].max())
            ideal_worst.append(weighted_data.iloc[:, i].min())
        else:
            ideal_best.append(weighted_data.iloc[:, i].min())
            ideal_worst.append(weighted_data.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    dist_best = np.sqrt(((weighted_data - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted_data - ideal_worst) ** 2).sum(axis=1))

    scores = dist_worst / (dist_best + dist_worst)

    df["Topsis Score"] = scores
    df["Rank"] = df["Topsis Score"].rank(ascending=False, method="dense")

    df.to_csv(output_file, index=False)
    return "success"