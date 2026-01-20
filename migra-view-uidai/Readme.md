# 📊 Migra-View: Predictive Aadhaar Intelligence  
Unlocking Societal Trends for Data-Driven Policy Intervention

---

## 🌟 Project Vision  
**Migra-View** is an advanced analytics framework designed for the **UIDAI Data Hackathon 2026**.  
By leveraging anonymized Aadhaar enrolment and update datasets, Migra-View identifies high-velocity population shifts and infrastructure demand.

It transforms raw administrative data into actionable **Micro-Trends**, enabling the government to deploy resources where they are needed most — *before the surge happens*.

---

## 🚀 Key Value Propositions

### ✅ Infrastructure Stress Forecasting  
Predicts demand for Aadhaar Seva Kendras (ASK) with high precision.

### ✅ Migration Hotspot Detection  
Uses biometric update spikes as a proxy for labor and student migration.

### ✅ Policy-Ready Dashboards  
An interactive Streamlit interface for non-technical decision-makers.

---

## 🛠 Tech Stack

| Category        | Tools / Technologies                          |
|-----------------|-----------------------------------------------|
| **Language**    | Python 3.11+                                  |
| **Modeling**    | Facebook Prophet (Time-Series Forecasting)    |
| **Dashboard**   | Streamlit                                     |
| **Visualization** | Plotly, Seaborn, Matplotlib                |
| **Data Handling** | Pandas, NumPy                              |

---

## 📁 Project Structure

```
migra-view-uidai/
├── data/
│   ├── raw/                # Original datasets from =
    └── processed/          # Merged, cleaned, and engineered CSVs
├── notebooks/              # Step-by-step development & EDA
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda_and_uii.ipynb
│   └── 03_predictive_modeling.ipynb
├── src/                    # Production-grade helper functions
│   ├── __init__.py
│   ├── data_utils.py       # Data pipeline & cleaning logic
│   └── plot_utils.py       # Reusable visualization & modeling functions
├── app/
│   └── dashboard.py        # Interactive Streamlit application
├── docs/                   # Presentation PDF and detailed reports
├── requirements.txt        # Project dependencies
└── README.md               # Project overview
```

---

## 📈 Model Performance & Insights

### **The Pitch Statement**
> “Our Migra-View engine achieved a **93.1% median accuracy rate (MDAPE)** for week-ahead infrastructure demand forecasting.  

> By monitoring the **RMSE ($2.8 × 10^7$)** to capture high-variance biometric shifts, our framework ensures that sudden migration spikes—often invisible in monthly aggregates—are flagged as high-priority zones for immediate policy intervention.”

---

## 🧠 Technical Rigor  

### **Why MDAPE?**  
We utilize **Median Absolute Percentage Error** instead of standard MAPE to remain robust against outliers, providing a truer reflection of performance across diverse Indian districts.

### **Why RMSE?**  
We track **Root Mean Squared Error** to penalize large forecasting misses.  
In public service, failing to predict a massive population surge is more critical than minor daily fluctuations.

### **Micro-Trend Detection**  
While the model is architected for yearly cycles (academic sessions, harvest migration), it has been optimized for short-term **Micro-Trends** to provide immediate value even from limited historical snapshots.

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/migra-view-uidai.git
cd migra-view-uidai
```

### 2. Set Up Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Run the Dashboard
```bash
streamlit run app/dashboard.py
```

---

## 💡 Policy Recommendations  

- **Dynamic Staffing:**  
  Scale ASK personnel in July–August based on forecasted school-enrolment spikes.

- **Mobile Units:**  
  Deploy Aadhaar-on-Wheels to districts identified as *High Intensity* in the Migra-View Hotspot Map.

- **Proactive Planning:**  
  Use the 90-day forecast to pre-allocate biometric kits to emerging industrial hubs.

---

## 🏛 Developed for the UIDAI Data Hackathon 2026  
**Unlocking the potential of data for a better-governed India.**

