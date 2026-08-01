-- Top 5 funds by AUM 
SELECT scheme_name, fund_house, aum_crore 
FROM fact_performance 
ORDER BY aum_crore DESC 
LIMIT 5; 
-- Average NAV per fund (top 10 highest) 
SELECT amfi_code, ROUND(AVG(nav), 2) AS avg_nav 
FROM fact_nav 
GROUP BY amfi_code 
ORDER BY avg_nav DESC 
LIMIT 10; 
-- Total transaction amount by type (SIP / Lumpsum / Redemption) 
SELECT transaction_type, SUM(amount_inr) AS total_amount, COUNT(*) AS 
num_transactions 
FROM fact_transactions 
GROUP BY transaction_type 
ORDER BY total_amount DESC; 
-- Transaction volume by state (top 10) 
SELECT state, COUNT(*) AS tx_count, SUM(amount_inr) AS total_amount 
FROM fact_transactions 
GROUP BY state 
ORDER BY total_amount DESC 
LIMIT 10; 
-- Funds with expense ratio under 1% 
SELECT scheme_name, fund_house, expense_ratio_pct 
FROM fact_performance 
WHERE expense_ratio_pct < 1.0 
ORDER BY expense_ratio_pct ASC; 
-- Top 5 funds by Sharpe ratio (best risk-adjusted return) 
SELECT scheme_name, fund_house, sharpe_ratio, return_3yr_pct 
FROM fact_performance 
ORDER BY sharpe_ratio DESC 
LIMIT 5; 
-- Average SIP amount by age group 
SELECT age_group, ROUND(AVG(amount_inr), 2) AS avg_sip_amount, COUNT(*) AS num_sips 
FROM fact_transactions 
WHERE transaction_type = 'Sip' 
GROUP BY age_group 
ORDER BY avg_sip_amount DESC; 
-- City tier (T30 vs B30) investment split 
SELECT city_tier, COUNT(*) AS tx_count, SUM(amount_inr) AS total_amount 
FROM fact_transactions 
GROUP BY city_tier; 
-- Funds that beat their benchmark (positive alpha) 
SELECT scheme_name, fund_house, alpha, return_3yr_pct, benchmark_3yr_pct 
FROM fact_performance 
WHERE alpha > 0 
ORDER BY alpha DESC; 
-- Fund manager details joined with performance (uses dim_fund + fact_performance) 
SELECT d.fund_manager, d.scheme_name, d.benchmark, p.sharpe_ratio, p.return_3yr_pct 
FROM dim_fund d 
JOIN fact_performance p ON d.amfi_code = p.amfi_code 
ORDER BY p.sharpe_ratio DESC 
LIMIT 10;