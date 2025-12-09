import csv
from pathlib import Path
from typing import Tuple
import matplotlib.pyplot as plt
import numpy as np

def load_precision_recall(csv_file: str) -> Tuple[np.ndarray, np.ndarray]:
    precision, recall = [], []
    csv_path = Path(csv_file)
    if not csv_path.exists():
        raise FileNotFoundError(csv_file)
    with open(csv_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            precision.append(float(row["precision"]))
            recall.append(float(row["recall"]))
    return np.array(precision), np.array(recall)

def plot_data(csv_file: str) -> None:
    precision, recall = load_precision_recall(csv_file)
    plt.figure(figsize=(6, 6))
    plt.plot(precision, recall, marker="o")
    plt.xlim(-0.05, 1.05)
    plt.ylim(-0.05, 1.05)
    plt.xlabel("Precision")
    plt.ylabel("Recall")
    plt.title("Precision–Recall Curve")
    plt.grid(True)
    plt.show()
