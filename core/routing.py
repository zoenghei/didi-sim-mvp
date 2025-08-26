# core/routing.py
from .config import CELL_KM, BASE_SPEED_KMH

def manhattan_dist(a, b, km_per_cell: float = CELL_KM) -> float:
    """曼哈顿距离（公里）"""
    return (abs(a[0]-b[0]) + abs(a[1]-b[1])) * km_per_cell

def manhattan_eta(a, b, congestion: float = 1.0) -> float:
    """ETA（分钟）= 距离 / 有效速度"""
    dist_km = manhattan_dist(a, b)
    effective_speed = BASE_SPEED_KMH / congestion  # km/h
    return (dist_km / effective_speed) * 60.0
