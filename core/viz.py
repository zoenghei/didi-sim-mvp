import folium
from typing import List, Tuple
from core.config import GRID_N

def grid_map():
    """生成基础网格地图"""
    m = folium.Map(location=[0, 0], zoom_start=13, control_scale=True)
    step = 0.001  # 控制可视化缩放比例
    for i in range(GRID_N):
        folium.PolyLine([(i*step, 0), (i*step, (GRID_N-1)*step)], opacity=0.3).add_to(m)
        folium.PolyLine([(0, i*step), ((GRID_N-1)*step, i*step)], opacity=0.3).add_to(m)
    return m, step

def plot_points(m, points: List[Tuple[int, int]], step: float, tooltip=""):
    """绘制点（乘客/司机）"""
    for (x, y) in points:
        folium.CircleMarker(
            location=[x*step, y*step],
            radius=4,
            tooltip=tooltip,
            opacity=0.8,
            color="blue" if tooltip=="Driver" else "red",
            fill=True
        ).add_to(m)

def plot_path(m, path: List[Tuple[int, int]], step: float):
    """绘制路径（简单直线连接起点和终点）"""
    coords = [(x*step, y*step) for (x, y) in path]
    folium.PolyLine(coords, weight=4, opacity=0.8, color="green").add_to(m)
    return m
