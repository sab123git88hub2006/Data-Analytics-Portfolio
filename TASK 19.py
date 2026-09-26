# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 17:38:00 2026

@author: sabiya
"""

import matplotlib.pyplot as plt
import pandas as pd

# 1. Read the Excel or CSV file
df = pd.read_excel("C:\\Users\\shami\\Downloads\\Sample-Superstore.xlsx",
                   sheet_name="Raw data-Orders")

# 2. Group sales by product name & sort descending
product_sales = (
    df.groupby("Product Name")["Sales"].sum()
    .reset_index()
    .sort_values(by="Sales", ascending=False))

product_sales["Rank"] = product_sales["Sales"].rank(
    method="min", ascending=False).astype(int)

top_10 = product_sales.head(10)

# Display Top 10 Table data
print()
print("*********-Top 10 Products by Sales-************")
print(top_10[["Rank", "Product Name", "Sales"]].to_string(index=False))

has_ties = top_10["Sales"].duplicated().any()
print(f"\nAny ties in Top 10?: {has_ties}")

# Display Chart
plt.figure(figsize=(10, 6))
plt.barh(top_10["Product Name"], top_10["Sales"], color="teal")
plt.xlabel("Total Sales ($)")
plt.ylabel("Product Name")
plt.title("Top 10 Products by Total Sales")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()