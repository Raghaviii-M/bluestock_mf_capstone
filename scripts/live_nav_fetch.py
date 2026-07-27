import requests
import pandas as pd
import os

# The 6 schemes we need: HDFC Top 100 + 5 key schemes

SCHEMES = {
    125497: "hdfc_top_100",
    119551: "sbi_bluechip",
    120503: "icici_bluechip",
    118632: "nippon_large_cap",
    119092: "axis_bluechip",
    120841: "kotak_bluechip",
}

OUTPUT_FOLDER = "data/raw"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Loop through each scheme, fetch, and save

for code, label in SCHEMES.items():
    url = f"https://api.mfapi.in/mf/{code}"
    print(f"\nFetching {label} (code {code}) from {url} ...")

    response = requests.get(url)
    payload = response.json()          # convert JSON text into a Python dict

    scheme_name = payload["meta"]["scheme_name"]
    records = payload["data"]          # list of {"date": ..., "nav": ...}

    df = pd.DataFrame(records)
    df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
    df["nav"] = df["nav"].astype(float)
    df["scheme_code"] = code
    df["scheme_name"] = scheme_name
    df = df.sort_values("date")        # oldest to newest

    save_path = os.path.join(OUTPUT_FOLDER, f"live_nav_{label}.csv")
    df.to_csv(save_path, index=False)

    print(f"Saved {len(df)} rows to {save_path}")
    print(f"Latest NAV: {df['nav'].iloc[-1]} on {df['date'].iloc[-1].date()}")

print("\nAll 6 live NAV fetches complete.")