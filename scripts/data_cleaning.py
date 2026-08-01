import pandas as pd

nav = pd.read_csv("data/raw/02_nav_history.csv")
tx = pd.read_csv("data/raw/08_investor_transactions.csv")
perf = pd.read_csv("data/raw/07_scheme_performance.csv")

print("NAV shape:", nav.shape)
print("Transactions shape:", tx.shape)
print("Performance shape:", perf.shape)

# --- Clean nav_history ---
nav['date'] = pd.to_datetime(nav['date'])
nav = nav.sort_values(['amfi_code', 'date'])
nav = nav.drop_duplicates()
nav['nav'] = nav.groupby('amfi_code')['nav'].ffill()

invalid_nav = nav[nav['nav'] <= 0]
print(f"Invalid NAV rows found: {len(invalid_nav)}")

nav.to_csv("data/processed/02_nav_history_clean.csv", index=False)
print("Saved cleaned NAV file.")

# --- Clean investor_transactions ---
tx['transaction_date'] = pd.to_datetime(tx['transaction_date'])
tx['transaction_type'] = tx['transaction_type'].str.strip().str.title()
tx = tx[tx['amount_inr'] > 0]

print("KYC status values:", tx['kyc_status'].unique())

tx.to_csv("data/processed/08_investor_transactions_clean.csv", index=False)
print("Saved cleaned transactions file.")

# --- Clean scheme_performance ---
numeric_cols = ['return_1yr_pct','return_3yr_pct','return_5yr_pct','sharpe_ratio']
for col in numeric_cols:
    perf[col] = pd.to_numeric(perf[col], errors='coerce')

perf['expense_flag'] = ~perf['expense_ratio_pct'].between(0.1, 2.5)
print("Rows with suspicious expense ratio:", perf['expense_flag'].sum())

perf.to_csv("data/processed/07_scheme_performance_clean.csv", index=False)
print("Saved cleaned performance file.")

from sqlalchemy import create_engine

engine = create_engine("sqlite:///data/db/bluestock_mf.db")

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
fund_master.to_sql('dim_fund', engine, if_exists='replace', index=False)

nav.to_sql('fact_nav', engine, if_exists='replace', index=False)
tx.to_sql('fact_transactions', engine, if_exists='replace', index=False)
perf.to_sql('fact_performance', engine, if_exists='replace', index=False)

print("All tables loaded into bluestock_mf.db")