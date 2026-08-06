# Bluestock Mutual Fund Analytics Capstone

## Project Overview

This project builds an end-to-end data pipeline for Indian mutual fund analytics:
ingesting raw AMFI/mfapi.in-based datasets, cleaning and structuring them into a
relational database, exploring trends visually, computing performance and risk
metrics, and preparing the ground for an interactive dashboard.

## Objective

To build an ETL pipeline that loads mutual fund datasets, validates and cleans them,
fetches live NAV data from mfapi.in, structures everything into a SQLite star-schema
database, explores the data visually, computes risk-adjusted performance metrics for
every scheme, and prepares clean, query-ready data for a dashboard.

## Technologies Used

- Python (Pandas, NumPy, SciPy)
- SQLite + SQLAlchemy
- Matplotlib, Seaborn, Plotly
- Requests (API calls to mfapi.in)
- Jupyter Notebook
- Power BI
- Git & GitHub

## Folder Structure

```
bluestock_mf_capstone/
├── data/
│   ├── raw/            # Original untouched CSVs (10 provided datasets + live NAV fetches)
│   ├── processed/       # Cleaned CSVs after Day 2 cleaning
│   └── db/              # bluestock_mf.db - SQLite database
├── notebooks/           # Jupyter notebooks: cleaning, EDA, performance analytics
├── dashboard/
│   └── charts/           # Exported PNG charts from EDA and performance analysis
├── scripts/             # Python scripts (ingestion, cleaning, verification)
├── sql/                 # schema.sql and queries.sql
├── reports/             # data_dictionary.md, cagr_report.csv, alpha_beta.csv,
│                         # fund_scorecard.csv, data quality notes
├── requirements.txt
└── README.md
```

## Progress So Far

### Day 1 — Project Setup + Data Ingestion (Complete)
- Set up project folder structure and Git repository
- Installed all required dependencies (see `requirements.txt`)
- Loaded and inspected all 10 provided datasets with Pandas
- Fetched live NAV data from the mfapi.in API for 5 key schemes (SBI Bluechip, ICICI
  Bluechip, Nippon Large Cap, Axis Bluechip, Kotak Bluechip)
- Validated that all AMFI codes in the fund master exist in the NAV history data

**Deliverables:** `Data_ingestion.py`, `live_nav_fetch.py`, `requirements.txt`, raw CSVs in `data/raw/`

### Day 2 — Data Cleaning + SQL Database Design (Complete)
- Cleaned `nav_history`, `investor_transactions`, and `scheme_performance` datasets —
  parsed dates, forward-filled missing NAVs, removed duplicates, validated all
  numeric fields (zero nulls, zero invalid rows found after cleaning)
- Designed a 4-table relational schema: `dim_fund`, `fact_nav`, `fact_transactions`,
  `fact_performance`
- Loaded all cleaned data into a SQLite database (`bluestock_mf.db`)
- Verified row counts match source files (46,000 NAV rows, 32,778 transactions,
  40 funds) and confirmed all foreign keys are consistent
- Wrote and tested 10 analytical SQL queries covering AUM ranking, Sharpe ratio
  ranking, state-wise transaction volume, and benchmark comparison
- Documented every table and column in `data_dictionary.md`

**Deliverables:** cleaned CSVs in `data/processed/`, `bluestock_mf.db`, `sql/schema.sql`,
`sql/queries.sql`, `reports/data_dictionary.md`

### Day 3 — Exploratory Data Analysis (Complete)
- Queried cleaned data directly from the SQLite database for analysis
- Built 15+ charts covering: NAV trends for all 40 schemes, AUM growth by fund house,
  SIP inflow trends, category-wise inflow heatmap, investor demographics (age, gender),
  geographic distribution (state, city tier), folio count growth, NAV return correlation
  matrix, and sector allocation across equity holdings
- Documented 10 key findings alongside each chart in Markdown cells

**Deliverables:** `notebooks/eda_analysis.ipynb`, 15+ exported PNG charts in `dashboard/charts/`

### Day 4 — Fund Performance Analytics (Complete)
- Computed daily returns for all 40 schemes and validated the distribution
- Calculated 1yr/3yr/5yr CAGR for every fund
- Computed Sharpe Ratio and Sortino Ratio (risk-adjusted return metrics) using a
  6.5% risk-free rate assumption, and ranked all funds
- Computed Alpha and Beta for each fund via OLS regression against the Nifty 100
  benchmark index
- Computed Maximum Drawdown and identified the worst decline period per fund
- Built a composite Fund Scorecard (0–100) combining return, Sharpe, alpha, expense
  ratio, and drawdown into a single ranking
- Plotted the top 5 funds against Nifty 50 and Nifty 100 over a 3-year window and
  computed tracking error for each

**Deliverables:** `notebooks/04_performance_analytics.ipynb`, `reports/cagr_report.csv`,
`reports/alpha_beta.csv`, `reports/fund_scorecard.csv`, benchmark comparison chart PNG

## Data Sources

All data is derived from publicly available AMFI India data and the mfapi.in API.
Investor transaction data is synthetically generated using realistic Indian mutual
fund market distributions. This project is for educational purposes only and does
not constitute financial advice.

