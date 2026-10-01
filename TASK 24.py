# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
Owner- Sabiya
"""

import pandas as pd

# Display options setup (Max 100 rows)
pd.set_option('display.max_rows', 100)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

excel_file = 'C:\\Users\\shami\\Downloads\\retail_sales_dataset (1).xlsx'
xls = pd.ExcelFile(excel_file)

customers_df = pd.read_excel(xls, 'Customers')
products_df = pd.read_excel(xls, 'Products')
stores_df = pd.read_excel(xls, 'Stores')
transactions_df = pd.read_excel(xls, 'Transactions')

dfs = {'Customers': customers_df,
       'Products': products_df,
       'Stores': stores_df,
       'Transactions': transactions_df}

issue_logs = []
def log_issue(dataset, issue_type, rule_description, severity, count, sample_ids):
    issue_logs.append({
        'Dataset': dataset,
        'Issue Type': issue_type,
        'Rule Description': rule_description,
        'Severity': severity,
        'Affected Count': count,
        'Sample Impacted IDs': str(sample_ids)})


# 1. Null Checks
null_counts_by_col = sum(df.isnull().sum().sum() for df in dfs.values())
for name, df in dfs.items():
    null_counts = df.isnull().sum()
    for col, null_c in null_counts.items():
        if null_c > 0:
            log_issue(name, 'Missing Data', f'Column `{col}` has missing values', 'High', null_c, [])

    dup_c = df.duplicated().sum()
    if dup_c > 0:
        log_issue(name, 'Duplicate Data', 'Complete duplicate rows found', 'Medium', dup_c, [])

# 2. Primary Key Uniqueness Check
pk_mapping = [('Customers', customers_df, 'CustomerID'),
              ('Products', products_df, 'ProductID'),
              ('Stores', stores_df, 'StoreID'),
              ('Transactions', transactions_df, 'TransactionID')]

pk_dups_count = 0
for name, df, pk_col in pk_mapping:
    pk_dups = df[df[pk_col].duplicated()]
    if len(pk_dups) > 0:
        pk_dups_count += len(pk_dups)
        log_issue(name, 'Uniqueness Violation', f'Duplicate primary key `{pk_col}`', 'Critical', len(pk_dups), pk_dups[pk_col].tolist()[:5])

# 3. Product Price & Cost Range Check
invalid_prices = products_df[
    (products_df['UnitPrice'] <= 0) | 
    (products_df['CostPrice'] <= 0) | 
    (products_df['CostPrice'] > products_df['UnitPrice'])
]
invalid_price_count = len(invalid_prices)
if invalid_price_count > 0:
    log_issue('Products', 'Range/Logic Error', 'Invalid product price/cost logic', 'High', invalid_price_count, invalid_prices['ProductID'].tolist()[:5])

# 4. Temporal/Date Logic Check
merged_tx = transactions_df.merge(customers_df[['CustomerID', 'JoinDate']], on='CustomerID', how='left')
tx_before_join = merged_tx[merged_tx['Date'] < merged_tx['JoinDate']]
date_logic_count = len(tx_before_join)

if date_logic_count > 0:
    log_issue('Transactions', 'Consistency Error', 'Transaction date precedes Customer Join Date', 'High', date_logic_count, tx_before_join['TransactionID'].tolist()[:5])

# Prepare Issue Log DataFrame
issues_df = pd.DataFrame(issue_logs)

# Cleaned Sample (Excluding invalid date sequence rows)
valid_tx_ids = set(transactions_df['TransactionID']) - set(tx_before_join['TransactionID'])
cleaned_sample_df = transactions_df[transactions_df['TransactionID'].isin(valid_tx_ids)].head(100)

# Helper status generator function
def get_check_status(count_val, custom_msg=None):
    if count_val == 0:
        return "Passed"
    return custom_msg if custom_msg else f"Flagged ({count_val} issue{'s' if count_val > 1 else ''} found)"


print()
print()
print("------------------------------------AUDIT REPORT---------------------------------------")

print(f"Dataset Audited        : {excel_file}")
print(f"Total Sheets Inspected : {len(dfs)} ({', '.join(dfs.keys())})")
print(f"Total Rows Scanned     : {sum(len(df) for df in dfs.values()):,}")
print(f"Total Issues Flagged   : {len(issues_df)}")
print("\nSummary of Quality Checks:")
print(f"  - Primary Key Uniqueness     : {get_check_status(pk_dups_count)}")
print(f"  - Null/Missing Value Check   : {get_check_status(null_counts_by_col)}")
print(f"  - Product Price Logic Check  : {get_check_status(invalid_price_count)}")
print(f"  - Date Sequence Logic Check  : {get_check_status(date_logic_count, f'Flagged ({date_logic_count} transactions prior to customer join date)')}")
print("---------------------------------------------------------------------------------------\n")

# ISSUE LOG
print()
print("-------------------------------------ISSUE LOG-------------------------------------------")
if not issues_df.empty:
    print(issues_df.head(100).to_string(index=False))
else:
    print("No issues found.")
print("-----------------------------------------------------------------------------------------")

# CLEANED SAMPLE (MAX 100 ROWS)
print()
print()
print("---------------------------CLEANED SAMPLE (FIRST 100 ROWS)--------------------------------")
print(cleaned_sample_df.to_string(index=False))
print("------------------------------------------------------------------------------------------")