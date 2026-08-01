import sqlite3

conn = sqlite3.connect("data/db/bluestock_mf.db")

queries = {
    "Top 5 by AUM":
    """
    SELECT scheme_name, fund_house, aum_crore
    FROM fact_performance
    ORDER BY aum_crore DESC
    LIMIT 5;
    """,

    "Funds under 1% expense":
    """
    SELECT scheme_name, expense_ratio_pct
    FROM fact_performance
    WHERE expense_ratio_pct < 1.0;
    """,

    "Fund manager + Sharpe":
    """
    SELECT d.fund_manager,
           d.scheme_name,
           p.sharpe_ratio
    FROM dim_fund d
    JOIN fact_performance p
      ON d.amfi_code = p.amfi_code
    ORDER BY p.sharpe_ratio DESC
    LIMIT 5;
    """
}

for label, query in queries.items():
    print(f"\n--- {label} ---")

    rows = conn.execute(query).fetchall()

    for row in rows:
        print(row)

conn.close()