# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 12:47:32 2026

@author: shami
"""

import pandas as pd

# Load dataset correctly (removed the extra df line)
df = pd.read_csv("Titanic-Dataset.csv")

# Select 3 numerical columns
cols = ['Age', 'Fare', 'SibSp']

# Calculate descriptive statistics individually
mean_vals = df[cols].mean()
median_vals = df[cols].median()
mode_vals = df[cols].mode().iloc[0]  # Take first mode
std_vals = df[cols].std()
q25_vals = df[cols].quantile(0.25)
q75_vals = df[cols].quantile(0.75)

summary_table = pd.DataFrame({
    'Mean': mean_vals,
    'Median': median_vals,
    'Mode': mode_vals,
    'Std Dev': std_vals,
    '25th Percentile': q25_vals,
    '75th Percentile': q75_vals
})

# Round to 2 decimal places for clean reading
print(summary_table.round(2))

