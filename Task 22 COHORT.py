# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 10:08:15 2026

@author: shami
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


csv_file_path = "C:\\Users\\shami\\OneDrive\\Desktop\\SABIYA\\online_retail_II.csv"
df = pd.read_csv(csv_file_path, encoding="ISO-8859-1")

' ---------------------------------------------------------'
'                 2. DATA CLEANING & PREPARATION'
' ---------------------------------------------------------'

df = df.dropna(subset=["Customer ID"])
df["Customer ID"] = df["Customer ID"].astype(int)

# Filter out non-positive quantities and zero/negative unit prices
df = df[(df["Quantity"] > 0) & (df["Price"] > 0)]

# Convert InvoiceDate to datetime format
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

'---------------------------------------------------------'
'          3. CALCULATE COHORTS & MONTH INDEXES            '
'---------------------------------------------------------'
# Create invoice month identifier
df["InvoiceMonth"] = df["InvoiceDate"].dt.to_period("M")

# Determine first purchase month for each unique customer
df["CohortMonth"] = df.groupby("Customer ID")["InvoiceMonth"].transform("min")

# Calculate offset in months (CohortIndex: 0 = signup month, 1 = month after, etc.)
invoice_year = df["InvoiceMonth"].dt.year
invoice_month = df["InvoiceMonth"].dt.month
cohort_year = df["CohortMonth"].dt.year
cohort_month = df["CohortMonth"].dt.month

years_diff = invoice_year - cohort_year
months_diff = invoice_month - cohort_month

df["CohortIndex"] = years_diff * 12 + months_diff

' ---------------------------------------------------------'
'               4. BUILD RETENTION MATRIX                  '
' ---------------------------------------------------------'
# Count unique active customers per CohortMonth and CohortIndex
cohort_data = (
    df.groupby(["CohortMonth", "CohortIndex"])["Customer ID"]
    .nunique()
    .reset_index()
)

# Pivot into matrix (Rows = Cohort Signup Month, Columns = Month Offset)
cohort_counts = cohort_data.pivot(
    index="CohortMonth", columns="CohortIndex", values="Customer ID"
)

# Calculate retention rates as percentages (%)
cohort_sizes = cohort_counts.iloc[:, 0]
retention = cohort_counts.divide(cohort_sizes, axis=0) * 100

'---------------------------------------------------------'
'                   5. HEATMAP VISUALIZATION              '
' ---------------------------------------------------------'
plt.figure(figsize=(13, 7.5), dpi=100)
ax = plt.gca()

# Draw visual grid using Matplotlib imshow
im = ax.imshow(retention.values, cmap="YlGnBu", aspect="auto")

# Formulate axis ticks and labels
y_labels = [str(x) for x in retention.index]
x_labels = [f"M+{int(x)}" for x in retention.columns]

ax.set_xticks(np.arange(len(x_labels)))
ax.set_yticks(np.arange(len(y_labels)))
ax.set_xticklabels(x_labels, fontsize=10)
ax.set_yticklabels(y_labels, fontsize=10)

# Overlay matrix cell annotations with dynamic text color
for i in range(len(y_labels)):
    for j in range(len(x_labels)):
        val = retention.values[i, j]
        if not np.isnan(val):
            text_color = "white" if val > 50 else "black"
            ax.text(
                j,
                i,
                f"{val:.1f}%",
                ha="center",
                va="center",
                color=text_color,
                fontsize=8.5,
                weight="bold",
            )

# Formatting chart titles and labels
plt.title("Customer Cohort Retention Rate (%)", fontsize=14, pad=15, weight="bold")
plt.xlabel("Cohort Period (Months Since First Purchase)", fontsize=11, labelpad=10)
plt.ylabel("Signup Cohort (Year-Month)", fontsize=11, labelpad=10)

# Colorbar setup
cbar = plt.colorbar(im)
cbar.set_label("Retention Rate (%)", fontsize=10)

plt.tight_layout()
plt.show()

' ---------------------------------------------------------'
'                 6. OUTPUT SUMMARY IN CONSOL               '
' ---------------------------------------------------------'
print("\n----- COHORT RETENTION PERCENTAGE TABLE -----")
print(retention.round(1).fillna("-"))