# Bluestock Mutual Fund Analytics Capstone

Individual capstone project — Bluestock Fintech Internship.

## Project Overview

This project builds an end-to-end data pipeline for Indian mutual fund analytics:
ingesting raw AMFI/mfapi.in-based datasets, cleaning and structuring them into a
relational database, and preparing the ground for exploratory analysis, performance
metrics, and an interactive dashboard.

## Objective

To build an ETL pipeline that loads mutual fund datasets, validates and cleans them,
fetches live NAV data from mfapi.in, structures everything into a SQLite star-schema
database, and prepares clean, query-ready data for analytics and dashboard development.

## Technologies Used

- Python (Pandas, NumPy)
- SQLite 
- Requests (API calls to mfapi.in)
- VS code
- Git & GitHub

## Folder Structure

```
bluestock_mf_capstone/
├── data/
│   ├── raw/            # Original untouched CSVs (10 provided datasets + live NAV fetches)
│   ├── processed/       # Cleaned CSVs after Day 2 cleaning
│   └── db/              # bluestock_mf.db - SQLite database
├── notebooks/           # Jupyter notebooks for cleaning, EDA, analytics
├── scripts/             # Python scripts (ingestion, cleaning, verification)
├── sql/                 # schema.sql and queries.sql
├── reports/             # data_dictionary.md and data quality notes
├── dashboard/           # Power BI dashboard files (upcoming)
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

