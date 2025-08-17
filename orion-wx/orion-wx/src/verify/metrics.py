"""Verification metrics scaffolding: CRPS, Brier score."""
from typing import Sequence
import numpy as np

def brier_score(y_true: Sequence[int], p: Sequence[float]) -> float:
    y = np.asarray(y_true, dtype=float)
    p = np.asarray(p, dtype=float)
    return float(np.mean((p - y) ** 2))
