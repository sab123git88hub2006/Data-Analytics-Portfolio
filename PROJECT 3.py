# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:07:49 2026

@author: shami
"""

import pandas as pd
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt


#print('==========================================')
#print(' STEP 1: DATA LOADING & PREPROCESSING')
#print('==========================================')

# 1. Load Dataset
df = pd.read_csv('C:\\Users\\shami\\Downloads\\online_retail_II.csv')

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Clean pipeline
clean_df = df.dropna(subset=['Customer ID']).copy()
clean_df = clean_df[(clean_df['Quantity'] > 0) & (clean_df['Price'] > 0)]
clean_df['TotalSum'] = clean_df['Quantity'] * clean_df['Price']
clean_df['Customer ID'] = clean_df['Customer ID'].astype(int).astype(str)

print(f"Data Cleaned Successfully. Total valid rows: {len(clean_df):,}\n")

# ==========================================
# STEP 2: CALCULATING RFM METRICS
# ==========================================
snapshot_date = clean_df['InvoiceDate'].max() + dt.timedelta(days=1)

rfm = clean_df.groupby('Customer ID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,  # Recency
    'Invoice': 'nunique',                                     # Frequency
    'TotalSum': 'sum'                                         # Monetary
}).reset_index()

rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']

# ==========================================
# STEP 3: QUANTILE-BASED SCORING (1 to 4 Scale)
# ==========================================
r_labels = [4, 3, 2, 1]  # Lower recency = higher score
f_labels = [1, 2, 3, 4]
m_labels = [1, 2, 3, 4]

rfm['R_Score'] = pd.qcut(rfm['Recency'], q=4, labels=r_labels).astype(int)
rfm['F_Score'] = pd.qcut(rfm['Frequency'].rank(method='first'), q=4, labels=f_labels).astype(int)
rfm['M_Score'] = pd.qcut(rfm['Monetary'], q=4, labels=m_labels).astype(int)

rfm['RFM_Score'] = rfm[['R_Score', 'F_Score', 'M_Score']].sum(axis=1)

# ==========================================
# STEP 4: RULE-BASED CUSTOMER SEGMENTATION
# ==========================================
def segment_customer(row):
    score = row['RFM_Score']
    r = row['R_Score']
    f = row['F_Score']
    
    if score >= 10:
        return 'Champions'
    elif (r >= 3) and (f >= 3):
        return 'Loyal Customers'
    elif (r >= 3) and (f < 3):
        return 'Promising / New'
    elif (r == 2) and (f >= 2):
        return 'At Risk'
    else:
        return 'Lost Customers'

rfm['Segment'] = rfm.apply(segment_customer, axis=1)

# ==========================================
# STEP 5: PRINT DETAILED BREAKDOWN TO CONSOLE
# ==========================================
print("=" * 65)
print("             CUSTOMER SEGMENTATION BREAKDOWN TABLE             ")
print("=" * 65)

# Group and compute metrics for printing
summary_table = rfm.groupby('Segment').agg(
    Customer_Count=('CustomerID', 'count'),
    Avg_Recency=('Recency', 'mean'),
    Avg_Frequency=('Frequency', 'mean'),
    Avg_Monetary=('Monetary', 'mean'),
    Total_Revenue=('Monetary', 'sum')
).round(2)

# Calculate percentage share of customers
summary_table['Customer_%'] = (summary_table['Customer_Count'] / summary_table['Customer_Count'].sum() * 100).round(2)

# Reorder columns for clean display
summary_table = summary_table[['Customer_Count', 'Customer_%', 'Avg_Recency', 'Avg_Frequency', 'Avg_Monetary', 'Total_Revenue']]

# Print to console
print(summary_table.to_string())
print("=" * 65 + "\n")

# Save outputs
rfm.to_csv('Processed_RFM_Customer_Segments.csv', index=False)
summary_table.to_csv('Segment_Summary_Breakdown.csv')
print("Files successfully saved: 'Processed_RFM_Customer_Segments.csv' & 'Segment_Summary_Breakdown.csv'.\n")

# ==========================================
# STEP 6: MATPLOTLIB VISUALIZATION
# ==========================================
segment_counts = rfm['Segment'].value_counts()

plt.figure(figsize=(9, 5))
bars = plt.bar(segment_counts.index, segment_counts.values, color='#2c3e50', edgecolor='black')

for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 30, f"{yval:,}", ha='center', va='bottom', fontsize=10, fontweight='bold')

plt.title('Customer Segment Distribution', fontsize=13, fontweight='bold', pad=12)
plt.xlabel('Customer Segment', fontsize=11)
plt.ylabel('Number of Customers', fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.tight_layout()

plt.savefig('segment_distribution.png', dpi=300)
plt.show()