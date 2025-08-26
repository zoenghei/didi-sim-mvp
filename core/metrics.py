import pandas as pd

def compute_kpis(matches, total_requests=0):
    """
    输入: 匹配结果 (rid, did, eta, dist)
    输出: KPI DataFrame
    - total_requests: 请求总数
    - matched: 成功匹配数
    - unmatched: 未匹配数
    - match_rate: 匹配率
    - avg_wait: 平均等待时间 (分钟)
    - total_dist: 总行驶距离 (公里)
    """
    if not matches:
        return pd.DataFrame([{
            "total_requests": total_requests,
            "matched": 0,
            "unmatched": total_requests,
            "match_rate": "0%",
            "avg_wait": None,
            "total_dist": 0.0
        }])

    df = pd.DataFrame(matches, columns=["rid", "did", "eta", "dist"])
    return pd.DataFrame([{
        "total_requests": total_requests,
        "matched": len(df),
        "unmatched": total_requests - len(df),
        "match_rate": f"{len(df)/total_requests:.1%}" if total_requests > 0 else None,
        "avg_wait": df["eta"].mean(),
        "total_dist": df["dist"].sum()
    }])
