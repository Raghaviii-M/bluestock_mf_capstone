import pandas as pd
import os

#List of the 10 files 
RAW_FOLDER = "data/raw"

FILES = {
    "fund_master": "01_fund_master.csv",
    "nav_history": "02_nav_history.csv",
    "aum_by_fund_house": "03_aum_by_fund_house.csv",
    "monthly_sip_inflows": "04_monthly_sip_inflows.csv",
    "category_inflows": "05_category_inflows.csv",
    "industry_folio_count": "06_industry_folio_count.csv",
    "scheme_performance": "07_scheme_performance.csv",
    "investor_transactions": "08_investor_transactions.csv",
    "portfolio_holdings": "09_portfolio_holdings.csv",
    "benchmark_indices": "10_benchmark_indices.csv",
}

#Load every file into a dictionary

data = {}
for name, filename in FILES.items():
    path = os.path.join(RAW_FOLDER, filename)
    df = pd.read_csv(path)
    data[name] = df
    print(f"\nLoaded '{name}' from {filename}")


#Print shape, dtypes, and head for every dataset

print("\n" + "=" * 70)
print("STEP 3: DATASET OVERVIEW")
print("=" * 70)

for name, df in data.items():
    print(f"\n--- {name} ---")
    print("Shape:", df.shape)
    print("\nColumn types:\n", df.dtypes)
    print("\nFirst 5 rows:\n", df.head())

# Check for missing values (anomalies) in every dataset
print("\n" + "=" * 70)
print("ANOMALY CHECK: Missing values per dataset")
print("=" * 70)

anomaly_notes = []
for name, df in data.items():
    missing = df.isnull().sum()
    missing = missing[missing > 0]
    if len(missing) > 0:
        print(f"\n{name} has missing values:\n{missing}")
        anomaly_notes.append(f"{name}: missing values in {list(missing.index)}")
    else:
        print(f"\n{name}: no missing values")

#Explore the fund_master file
print("\n" + "=" * 70)
print("STEP 6: FUND MASTER EXPLORATION")
print("=" * 70)

fund_master = data["fund_master"]

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub-Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())

print("\nSample AMFI codes:")
print(fund_master["amfi_code"].head().tolist())


# Validate AMFI codes: does every fund_master code exist in nav_history?
print("\n" + "=" * 70)
print("STEP 7: AMFI CODE VALIDATION")
print("=" * 70)

nav_history = data["nav_history"]

fund_master_codes = set(fund_master["amfi_code"])
nav_history_codes = set(nav_history["amfi_code"])

missing_codes = fund_master_codes - nav_history_codes

if missing_codes:
    print(f"\nWARNING: {len(missing_codes)} codes in fund_master have NO nav_history data:")
    print(missing_codes)
    validation_note = f"{len(missing_codes)} scheme(s) missing NAV history: {missing_codes}"
else:
    print("\nAll fund_master codes have matching NAV history. PASS.")
    validation_note = "All AMFI codes matched successfully between fund_master and nav_history."


# Save a short data quality summary to reports/
os.makedirs("reports", exist_ok=True)
summary_path = "reports/data_quality_summary.txt"

with open(summary_path, "w") as f:
    f.write("DATA QUALITY SUMMARY - Day 1\n")
    f.write("=" * 40 + "\n\n")
    f.write(f"Total datasets loaded: {len(data)}\n\n")
    f.write("Missing value anomalies:\n")
    if anomaly_notes:
        for note in anomaly_notes:
            f.write(f"- {note}\n")
    else:
        f.write("- None found\n")
    f.write("\nAMFI code validation:\n")
    f.write(f"- {validation_note}\n")

print(f"\nData quality summary saved to: {summary_path}")
print("\nDay 1 data ingestion complete.")