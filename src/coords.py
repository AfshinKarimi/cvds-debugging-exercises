import numpy as np
def swap(coords: np.ndarray) -> np.ndarray:
    if coords.ndim != 2 or coords.shape[1] != 5:
        raise ValueError("coords must have shape (N, 5).")
    swapped = coords.copy()
    swapped[:, 0], swapped[:, 1] = coords[:, 1], coords[:, 0]
    swapped[:, 2], swapped[:, 3] = coords[:, 3], coords[:, 2]
    return swapped
