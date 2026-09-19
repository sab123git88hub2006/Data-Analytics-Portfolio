# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 16:13:43 2026

@author: Sabiya
"""

import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)     
pd.set_option('display.max_rows', None)

d = "TASK 12.xlsx" 
df = pd.read_excel(d)

print(df.head())

# Count null values
missing_vals = df.isnull().sum()

# Calculate percentage of missing values per column
missing_percentage = (df.isnull().sum() / len(df)) * 100

# Create a clean summary DataFrame
missing_summary = pd.DataFrame({
    'Missing Count': missing_vals,
    'Percentage': missing_percentage.round(2)
})

missing_summary = missing_summary[missing_summary['Missing Count'] > 0]
print()
print()
print("--- MISSING VALUE SUMMARY ---")
print(missing_summary)
