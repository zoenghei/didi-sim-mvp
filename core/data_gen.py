import numpy as np
import pandas as pd
from .config import GRID_N, RANDOM_SEED

np.random.seed(RANDOM_SEED)

def gen_requests(n_requests=200):
    origins = [(np.random.randint(0, GRID_N), np.random.randint(0, GRID_N)) for _ in range(n_requests)]
    dests = [(np.random.randint(0, GRID_N), np.random.randint(0, GRID_N)) for _ in range(n_requests)]
    ts = np.linspace(0, 60, n_requests)
    return pd.DataFrame({"id": range(n_requests), "origin": origins, "dest": dests, "ts": ts})

def gen_drivers(n_drivers=50):
    pos = [(np.random.randint(0, GRID_N), np.random.randint(0, GRID_N)) for _ in range(n_drivers)]
    return pd.DataFrame({"id": range(n_drivers), "pos": pos, "capacity": [2]*n_drivers})
