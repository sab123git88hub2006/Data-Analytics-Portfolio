# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 20:36:56 2026

@author: sabiya
"""

import pandas as pd

# 1. Configure Pandas to display ALL columns and rows without truncation
pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)
pd.set_option("display.width", 1000)
pd.set_option("display.max_colwidth", None)


df = pd.read_csv("C:\\Users\\shami\\Downloads\\Year 2009-2010.csv",
                 encoding="latin1")

df_clean = df.dropna(subset=["Description"])
df_clean = df_clean[~df_clean["Invoice"].astype(str).str.startswith("C")]
df_clean = df_clean[df_clean["Quantity"] > 0]

# 4. Extract unique items per order
basket_items = df_clean[["Invoice", "Description"]].drop_duplicates()
merged = pd.merge(
    basket_items, basket_items, on="Invoice", suffixes=("_1", "_2")
)
pairs = merged[merged["Description_1"] < merged["Description_2"]]
pair_counts = (
    pairs.groupby(["Description_1", "Description_2"])
    .size()
    .reset_index(name="Times Bought Together")
)
top_product_pairs = (
    pair_counts.sort_values(by="Times Bought Together", ascending=False)
    .head(10)
    .reset_index(drop=True)
)

# Display full DataFrame output with all rows and columns
print()
print("Product Basket Analysis")
print()
print(top_product_pairs)