from .config import ETA_LIMIT_MIN

def baseline_match(requests, drivers, eta_fn, dist_fn):
    """
    基准方案：每个乘客分配到最近的司机，不考虑ETA限制。
    返回: (rid, did, eta, dist)
    """
    matches = []
    for _, r in requests.iterrows():
        cands = []
        for _, d in drivers.iterrows():
            if d["capacity"] <= 0:
                continue
            eta = eta_fn(d["pos"], r["origin"])
            dist = dist_fn(d["pos"], r["origin"])
            cands.append((eta, d["id"], dist))
        if not cands:
            continue
        # 选择最近司机
        cands.sort()
        eta, did, dist = cands[0]
        drivers.loc[drivers.id == did, "capacity"] -= 1
        matches.append((r["id"], did, eta, dist))
    return matches


def greedy_match(requests, drivers, eta_fn, dist_fn):
    """
    优化方案：贪心匹配，要求ETA小于阈值。
    返回: (rid, did, eta, dist)
    """
    matches = []
    for _, r in requests.iterrows():
        cands = []
        for _, d in drivers.iterrows():
            if d["capacity"] <= 0:
                continue
            eta = eta_fn(d["pos"], r["origin"])
            if eta <= ETA_LIMIT_MIN:
                dist = dist_fn(d["pos"], r["origin"])
                cands.append((eta, d["id"], dist))
        if not cands:
            continue
        # 贪心选择ETA最小的司机
        cands.sort()
        eta, did, dist = cands[0]
        drivers.loc[drivers.id == did, "capacity"] -= 1
        matches.append((r["id"], did, eta, dist))
    return matches
