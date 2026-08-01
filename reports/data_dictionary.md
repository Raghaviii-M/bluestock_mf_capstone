# Data Dictionary

# Dataset 1 : NAV History

**File Name:** `02_nav_history_clean.csv`

### Description

Contains the historical Net Asset Value (NAV) of mutual fund schemes. The data is cleaned by converting dates into a standard format, removing duplicates, validating NAV values, and sorting records by scheme and date.

| Column    | Data Type | Business Definition                               |
|-----------|-----------|---------------------------------------------------|
| amfi_code | Integer   | Unique AMFI code identifying a mutual fund scheme |
| date      | Date      | Date on which the NAV was recorded                |
| nav       | Decimal   | Net Asset Value of one unit of the mutual fund    |

---

# Dataset 2 : Scheme Performance

**File Name:** `07_scheme_performance_clean.csv`

### Description

Contains mutual fund performance indicators, returns, risk measures, Assets Under Management (AUM), and expense ratios for different schemes.

| Column             | Data Type |                     BusinessDefinition                                                          ||--------------------|-----------|-------------------------------------------------------------------------------|
| amfi_code          | Integer   | Unique scheme identifier                                                     |
| scheme_name        | Text      | Name of the mutual fund scheme                                               |
| fund_house         | Text      | Asset Management Company managing the fund                                   |
| category           | Text      | Category of the mutual fund                                                  |
| plan               | Text      | Investment plan (Regular or Direct)                                          |
| return_1yr_pct     | Decimal   | Return generated over the last 1 year (%)                                    |
| return_3yr_pct     | Decimal   | Return generated over the last 3 years (%)                                   |
| return_5yr_pct     | Decimal   | Return generated over the last 5 years (%)                                   |
| benchmark_3yr_pct  | Decimal   | Three-year benchmark return (%)                                              |
| alpha              | Decimal   | Excess return generated compared to the benchmark                            |
| beta               | Decimal   | Measure of fund volatility compared to the market                            |
| sharpe_ratio       | Decimal   | Risk-adjusted return of the scheme                                           |
| sortino_ratio      | Decimal   | Downside risk-adjusted performance measure                                   |
| std_dev_ann_pct    | Decimal   | Annualized standard deviation of returns                                     |
| max_drawdown_pct   | Decimal   | Maximum observed decline from peak value                                     |
| aum_crore          | Decimal   | Assets Under Management in Crores (₹)                                        |
| expense_ratio_pct  | Decimal   | Annual expense ratio charged by the fund                                     |
| morningstar_rating | Integer   | Morningstar performance rating                                               |
| risk_grade         | Text      | Risk level assigned to the scheme                                            |
| expense_flag       | Text      | Indicates whether the expense ratio falls within the expected business range |

---

# Dataset 3 : Investor Transactions

**File Name:** `08_investor_transactions_clean.csv`

### Description

Contains investor transaction details including investments, redemptions, payment methods, investor demographics, and KYC information.

| Column             | Data Type | Business Definition                             |
|--------------------|-----------|-------------------------------------------------|
| investor_id        | Integer   | Unique identifier of the investor               |
| transaction_date   | Date      | Date on which the transaction occurred          |
| amfi_code          | Integer   | Mutual fund scheme code                         |
| transaction_type   | Text      | Type of transaction (SIP, Lumpsum, Redemption)  |
| amount_inr         | Decimal   | Transaction amount in Indian Rupees             |
| state              | Text      | State of the investor                           |
| city               | Text      | City of the investor                            |
| city_tier          | Text      | Classification of city (Tier 1, Tier 2, Tier 3) |
| age_group          | Text      | Age category of the investor                    |
| gender             | Text      | Gender of the investor                          |
| annual_income_lakh | Decimal   | Annual income in Lakhs                          |
| payment_mode       | Text      | Mode of payment used for the transaction        |
| kyc_status         | Text      | Indicates whether KYC verification is completed |

---

# Data Cleaning Summary

The following data quality checks were performed before loading the datasets into SQLite:

- Converted date columns into standard datetime format.
- Removed duplicate records.
- Sorted NAV history by AMFI code and date.
- Forward-filled missing NAV values where applicable.
- Verified NAV values are greater than zero.
- Standardized transaction type values.
- Validated transaction amounts are positive.
- Checked KYC status values for consistency.
- Converted return-related columns to numeric values.
- Verified expense ratios fall within the expected business range.

---

# Database Usage

The cleaned datasets are loaded into the SQLite database using SQLAlchemy and are used for analytical SQL queries, reporting, and dashboard development.