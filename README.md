# 📉 Lean Six Sigma Process Analytics: Cycle Time Reduction

![Tableau](https://img.shields.io/badge/Tableau-E97627?style=for-the-badge&logo=tableau&logoColor=white)
![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=databricks&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

> **DMAIC project reducing sales proposal cycle time by 15% — enhanced with a live Databricks monitoring pipeline for real-time process KPI tracking in Tableau.**

---

## 📌 Business Overview

Gentech, a $60B multinational, faced stagnating growth due to a sluggish Quote-to-Tender process. **Goal:** Reduce proposal cycle time by 15% using DMAIC methodology.

The control phase is powered by a **Databricks + Tableau live monitoring pipeline** ingesting CRM data daily and surfacing SLA breaches in real time — no manual reporting needed.

---

## 🔄 DMAIC Results

| Phase | Key Action | Outcome |
|-------|-----------|---------|
| **Define** | SIPOC map, defect definition (>35 days) | Baseline: 31.6 days avg, sigma 2.08 |
| **Measure** | Tableau control chart by brand/region | DPMO: 281,053 |
| **Analyze** | Fishbone diagram — approval loops, manual entry, sequential reviews | 3 root causes identified |
| **Improve** | RPA for standard bids, Poka-Yoke CRM validation, parallel reviews | Projected -4.7 days |
| **Control** | Databricks → Tableau live SLA dashboard | Automated breach alerts |

---

## 📈 Final Results

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Avg Cycle Time | 31.6 days | 26.9 days | **-15.2%** ✅ |
| Sigma Level | 2.08 | 2.78 | +0.70 |
| DPMO | 281,053 | 158,655 | -44% |
| Rework Rate | 12% | 2% | -83% |

---

## 🧠 Live Monitoring Pipeline

```
Salesforce CRM (daily export)
  → ADF → Databricks Delta: proposals_raw
    → dbt: proposal_kpis (cycle time, sigma, SLA status)
      → Tableau: real-time SLA monitoring + trend alerts
        → Email alert when 7-day avg > 30 days
```

---

## 🛠 Tools & Stack

| Category | Tools |
|----------|-------|
| Methodology | Lean Six Sigma DMAIC, SIPOC, Fishbone |
| Monitoring | Databricks, Delta Lake, ADF, dbt |
| Visualization | Tableau control charts, Draw.io |
| Statistics | Minitab (normality tests, sigma calculation) |

---

## 🚀 How to Run

```bash
git clone https://github.com/omkarpallerla/Lean-Six-Sigma-Process-Analytics.git
cd Lean-Six-Sigma-Process-Analytics
pip install -r requirements.txt
jupyter notebook notebooks/01_Baseline_Analysis.ipynb
```

---

<div align="center">
  <sub>Built by <a href="https://github.com/omkarpallerla">Omkar Pallerla</a> · MS Business Analytics, ASU · BI Engineer · Tableau | Databricks | Azure Certified</sub>
</div>