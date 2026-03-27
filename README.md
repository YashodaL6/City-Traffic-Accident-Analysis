# City-Traffic-Accident-Analysis
End-to-end city traffic accident analysis using  Python, SQL, and Power BI. Covers EDA, statistical  moments, data cleaning, and interactive dashboard  to identify high-risk zones and accident patterns.  Goal: reduce accidents by 20% using data insights.


# 🚦 City Traffic Accident Analysis

> **End-to-end data analytics project** analyzing 2,016 city traffic records to identify accident-prone zones, signal issues, and risk patterns — with the goal of reducing accidents by 20% through data-driven insights.

---

## 📌 Overview

Road accidents are a critical public safety challenge. This project performs a complete data analytics  on a city traffic accident dataset — from raw data exploration to an interactive Power BI dashboard and a professional presentation.

**Business Problem:** High number of accidents at intersections and highways due to unpredictable traffic, poorly timed signals, and adverse road conditions. No system exists to predict or warn about accident-prone areas.

**Business Objective:** Maximize accident pattern identification across high-risk zones.

**Success Criteria:** Reduce accidents at flagged high-risk zones by at least 20%.

---

## 📂 Dataset

| Attribute | Details |
|---|---|
| File | `Project_dataset_city_traffic_accident.xlsx` |  (Confidential)
| Total Records | 2,016 rows |
| Original Columns | 33 columns |
| Columns After Cleaning | 29 columns (4 removed) |
| Target Variable | `accident_occurred` (Boolean) |
| Accident Records | 93 (4.6% of dataset) |
| Geographic Scope | Hyderabad city area |
| Time Coverage | All 24 hours, all 7 days, monsoon season |

### Key Columns

| Column | Description |
|---|---|
| `location_id` | Unique intersection identifier |
| `road_type` | Highway / Urban / Rural  |
| `blackspot_score` | Location risk score (0.01 – 0.60) |
| `avg_speed_kmph` | Average vehicle speed |
| `vehicle_count_per_hr` | Hourly traffic volume |
| `has_signal` | Whether signal is present |
| `violations_count` | Signal violations recorded |
| `accident_occurred` | **Target variable** — True/False |
| `weather` | Weather condition at time of record |
| `lighting` | Lighting condition |
| `severity` | Accident severity (93 records only) |
| `cause` | Cause of accident (93 records only) |

---

## 🛠️ Tools & Technologies

| Tool | Purpose |
|---|---|
| **Python** | Data loading, EDA, cleaning, visualization |
| **Pandas** | Data manipulation and analysis |
| **Seaborn / Matplotlib** | Statistical visualizations |
| **SciPy** | Statistical moments (skewness, kurtosis) |
| **MySQL** | SQL-based EDA and querying |
| **Power BI Desktop** | Interactive dashboard |
| **Microsoft Excel** | Business moments analysis report |
| **Gamma** | Professional presentation (PPT) |

---

## 📁 Project Structure

```
city-traffic-accident-analysis/
│
├── data/
│   └── Project_dataset_city_traffic_accident.xlsx
│
├── python/
│   └── city_traffic_eda.py          # Full EDA code
│
├── sql/
│   └── city_traffic_queries.sql     # All 22 SQL queries
│
├── reports/
│   ├── EDA_Report.docx              # Detailed EDA report
│   ├── Business_Moments.xlsx        # Statistical moments analysis
│   └── Dashboard_Screenshot.png     # Power BI dashboard
│
├── presentation/
│   └── City_Traffic_Analysis.pptx   # Gamma presentation
│
└── README.md
```

---

## 🔢 Steps Performed

### Step 1 — Data Loading & Initial Exploration
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_excel('Project_dataset_city_traffic_accident.xlsx')
df.shape        # (2016, 33)
df.info()
df.describe()
df.isnull().sum().sort_values(ascending=False)
```

### Step 2 — Data Cleaning
- Removed 4 redundant columns (`peak`, `veh_count_at_accident`, 2 quality flags)
- Filled `lighting` NaN with `"Day"` (justified by hour_of_day analysis)
- Filled `weather` NaN with `"Unknown"` (no basis to infer)
- Cleaned `avg_speed_kmph` — replaced negatives and >150 with median
- Converted `day_of_week` and `hour_of_day` to object (category labels)
- Validated timestamp against derived columns — 100% match confirmed
- Validated `cycle_time_s` = `green + yellow + red` — confirmed

### Step 3 — Exploratory Data Analysis (EDA)

**Univariate Analysis**
- Histograms and boxplots for all 11 numeric columns
- 4 statistical moments: Mean/Median/Mode, Variance/StdDev, Skewness, Kurtosis

**Bivariate Analysis**
- All numeric columns analyzed against `accident_occurred`
- Categorical columns: weather, lighting, road_type, season, enforcement_level
- Boolean columns: has_signal, is_peak, signal_status

**Multivariate Analysis**
- Full Pearson correlation heatmap
- Key finding: `speed_limit` ↔ `avg_speed` = +0.89 (strongest pair)

### Step 4 — SQL Analysis (MySQL)
```sql
-- 22 queries covering:
-- Accident rate by hour, day, weather, lighting
-- Signal vs no-signal comparison
-- Top dangerous locations
-- Traffic density analysis
-- Enforcement level impact
-- Location + time + cause combined analysis
```

### Step 5 — Power BI Dashboard
- Single-page interactive dashboard
- 5 KPI cards, 10+ charts, location scatter plot
- Slicers: Season, Weather, Road Type, Signal, Peak
- Dark navy professional theme

### Step 6 — EDA Report (Word Document)
- 6-section professional report
- All charts embedded with statistical and business insights
- Complete data cleaning documentation
- ML readiness assessment

### Step 7 — Presentation (Gamma)
- Professional slides summarizing key findings
- Business recommendations
- Dashboard screenshots

---

## 📊 Dashboard

![City Traffic Accident Dashboard](reports/Dashboard_Screenshot.png)

### Dashboard Pages / Sections

| Section | Visuals |
|---|---|
| KPI Row | Total Records, Total Accidents, Accident Rate %, High Risk Zones, Total Violations |
| Row 1 | Accident Distribution (Donut), Accident Rate by Hour (Line), Accidents by Road Type,Top Causes (Bar) |
| Row 2 | Weather, Lighting, Signal Presence, Day of week (Bar charts) |
| Row 3 | Location Map (Scatter), Top 5 High Risk Table |

---

## 📈 Key Findings

- **Urban roads** have the highest accident count (77 out of 93)
- **Foggy and Rainy weather** show the highest accident rates (7.2% and 5.8%)
- **Dawn and Dusk** lighting conditions are disproportionately dangerous
- **Peak hours** (8–9 AM, 5–7 PM) show significantly higher accident rates
- **yellow_duration_s** has Skewness=9.62, Kurtosis=105.79 — signal malfunction detected at specific locations (max=65s vs standard 3–7s)
- **vehicle_count_per_hr** has Kurtosis=30.54 — extreme traffic spikes require adaptive signals
- **Speeding** and **Signal Violations** are the top 2 causes of accidents

---

## 🎯 Business Recommendations

1. **Deploy emergency signal inspection** at locations with blackspot_score > 0.50
2. **Implement adaptive signal timing** during peak hours at high-volume intersections
3. **Strengthen enforcement** on Urban roads — especially Fridays and Saturdays
4. **Issue weather and lighting alerts** during Fog, Rain, Dawn, and Dusk conditions
5. **Reduce red signal duration** below 60 seconds at low-traffic night hours

---

## ▶️ How to Run

### Python EDA
```bash
# 1. Install required libraries
pip install pandas numpy matplotlib seaborn scipy openpyxl

# 2. Run the EDA script
python python/city_traffic_eda.py
```

### SQL Queries
```sql
-- 1. Create database
CREATE DATABASE city_traffic_db;
USE city_traffic_db;

-- 2. Import the Excel file into MySQL
-- (Use MySQL Workbench → Table Data Import Wizard)

-- 3. Run queries from
-- sql/city_traffic_queries.sql
```

### Power BI Dashboard
```
1. Open Power BI Desktop
2. Get Data → Excel → data/Project_dataset_city_traffic_accident.xlsx
3. Apply Power Query transformations
4. Load the .pbix file or rebuild using the guide in reports/
```

---

## 📋 Requirements

```
Python       3.8+
pandas       1.3+
numpy        1.21+
matplotlib   3.4+
seaborn      0.11+
scipy        1.7+
openpyxl     3.0+
MySQL        8.0+
Power BI     Desktop (latest)
```

---

## 👤 Author

**YASHODA KRISHNA**
Data Analytics Project — City Traffic Accident Analysis
Tools: Python | SQL | Power BI | Excel | Gamma

---

## 📄 License

This project is for educational and portfolio purposes.

---

> *"Data-driven decisions save lives — identifying accident patterns is the first step toward safer roads."*
