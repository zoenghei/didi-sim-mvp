import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
from streamlit.components.v1 import html

from core.config import GRID_N
from core.data_gen import gen_requests, gen_drivers
from core.routing import manhattan_eta, manhattan_dist
from core.matching import greedy_match, baseline_match
from core.metrics import compute_kpis
from core.viz import grid_map, plot_points, plot_path

st.set_page_config(page_title="Didi-Sim MVP", layout="wide")
st.title("Didi-Like Ride-Hailing Simulator · MVP")

with st.sidebar:
    st.header("Parameters")
    n_drivers = st.slider("Drivers", 20, 200, 50, 10)
    n_requests = st.slider("Requests", 50, 500, 200, 50)
    congestion = st.slider("Congestion factor", 1.0, 2.0, 1.0, 0.1)
    run = st.button("Run Simulation")

if run:
    # 1. 数据生成
    req = gen_requests(n_requests)
    drv = gen_drivers(n_drivers)

    # 2. 匹配函数
    eta_fn = lambda a, b: manhattan_eta(a, b, congestion=congestion)

    # 基准方案
    base_matches = baseline_match(req.copy(), drv.copy(), eta_fn, manhattan_dist)
    base_kpi = compute_kpis(base_matches, total_requests=len(req))

    # 优化方案
    opt_matches = greedy_match(req.copy(), drv.copy(), eta_fn, manhattan_dist)
    opt_kpi = compute_kpis(opt_matches, total_requests=len(req))

    # 3. KPI 对比
    st.subheader("KPIs Comparison")
    st.write("Baseline KPIs:")
    st.dataframe(base_kpi, use_container_width=True)
    st.write("Optimized KPIs (Greedy):")
    st.dataframe(opt_kpi, use_container_width=True)

    # 计算路程降低率
    base_dist = base_kpi["total_dist"].iloc[0]
    opt_dist = opt_kpi["total_dist"].iloc[0]
    reduction = (base_dist - opt_dist) / base_dist * 100 if base_dist > 0 else 0
    st.metric("Distance Reduction (%)", f"{reduction:.1f}%")

    # 4. 可视化地图（仅显示优化方案示例）
    st.subheader("Map View (Optimized Example)")
    m, step = grid_map()

    req_points = [tuple(o) for o in req["origin"].head(50)]
    drv_points = [tuple(p) for p in drv["pos"].head(50)]
    plot_points(m, req_points, step, tooltip="Request")
    plot_points(m, drv_points, step, tooltip="Driver")

    for rid, did, eta, dist in opt_matches[:10]:
        r = req.loc[req.id == rid].iloc[0]
        path = [tuple(r["origin"]), tuple(r["dest"])]
        plot_path(m, path, step)

    html(m._repr_html_(), height=600)

else:
    st.info("Set parameters then click Run Simulation")
