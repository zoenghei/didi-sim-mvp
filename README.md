# Didi-Sim MVP 🚕  

## 项目背景  
在共享出行业务中，乘客等待时间长、司机利用率低是常见痛点。完整调度系统开发成本高，因此本项目尝试用 **最小可行产品 (MVP)** 思路，快速模拟和验证核心假设：  
- 是否可以通过算法优化，减少乘客平均等待时间？  
- 是否能够在拼车场景下，降低司机的整体行驶路程？  

---

## 核心方案  

### 1. 距离模型  
- 使用 **曼哈顿距离** 近似城市网格道路，更符合车辆实际行驶路径。  
- 结合速度和拥堵系数，估算 ETA（预计到达时间）。  

### 2. 匹配逻辑  
- **基准方案**：每个乘客分配到最近司机，不设限制。  
- **优化方案（贪婪算法）**：只在 ETA 阈值内匹配，并优先选择 ETA 最小的司机。  

### 3. 指标体系  
- 匹配率 (Match Rate)  
- 平均等待时间 (Avg Wait Time)  
- 总行驶路程 (Total Distance)  
- 路程降低率 (Distance Reduction %)  

---

## 使用方法  
```bash
pip install -r requirements.txt
streamlit run web/app.py

<img width="700" height="623" alt="image" src="https://github.com/user-attachments/assets/f6a58f82-e4ff-4fc6-9fe6-351b80aa9d1f" />
