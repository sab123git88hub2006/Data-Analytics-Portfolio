# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 20:14:48 2026

@author: Sabiya
"""

import pandas as pd
import numpy as np


df = pd.read_csv('C:\\Users\\shami\\Downloads\\online_retail_II.csv', encoding='latin1')


df_clean = df.dropna(subset=['Customer ID']).copy()
df_clean['CustomerID'] = df_clean['Customer ID'].astype(int)


df_clean = df_clean[~df_clean['Invoice'].astype(str).str.startswith('C')]
df_clean = df_clean[(df_clean['Quantity'] > 0) & (df_clean['Price'] > 0)]


df_clean['TotalPrice'] = df_clean['Quantity'] * df_clean['Price']
df_clean['InvoiceDate'] = pd.to_datetime(df_clean['InvoiceDate'], format='mixed')

# 3. Order-Level Aggregation
orders = df_clean.groupby(['CustomerID', 'Invoice']).agg(
    OrderDate=('InvoiceDate', 'min'),
    OrderValue=('TotalPrice', 'sum')
).reset_index()


orders['OrderRank'] = orders.groupby('CustomerID')['OrderDate'].rank(method='first')
orders['OrderType'] = np.where(orders['OrderRank'] == 1, 'First-Time', 'Repeat')

customer_summary = orders.groupby('CustomerID').agg(
    TotalOrders=('Invoice', 'count'),
    TotalSpend=('OrderValue', 'sum')
).reset_index()


total_customers = len(customer_summary)
repeat_customers = (customer_summary['TotalOrders'] > 1).sum()
one_time_customers = total_customers - repeat_customers
repeat_rate = (repeat_customers / total_customers) * 100

print(f"Total Unique Customers: {total_customers:,}")
print(f"One-Time Customers:    {one_time_customers:,}")
print(f"Repeat Customers:      {repeat_customers:,}")
print(f"Repeat Customer Rate:  {repeat_rate:.2f}%\n")


aov_df = orders.groupby('OrderType').agg(
    TotalOrders=('Invoice', 'count'),
    TotalRevenue=('OrderValue', 'sum'),
    AOV=('OrderValue', 'mean')
).reset_index()

print("--- Avg. Order Value COMPARISON ---")
print(aov_df.to_string(index=False))
print("\n")

# 6. Customer Segmentation
def get_segment(orders_count):
    if orders_count == 1:
        return 'One-Time Buyer (1 order)'
    elif orders_count == 2:
        return 'Returning Customer (2 orders)'
    elif 3 <= orders_count <= 5:
        return 'Frequent Customer (3-5 orders)'
    else:
        return 'Loyal Customer (6+ orders)'

customer_summary['Segment'] = customer_summary['TotalOrders'].apply(get_segment)

segment_table = customer_summary.groupby('Segment').agg(
    CustomerCount=('CustomerID', 'count'),
    TotalRevenue=('TotalSpend', 'sum'),
    AvgSpendPerCustomer=('TotalSpend', 'mean'),
    AvgOrdersPerCustomer=('TotalOrders', 'mean')
).reset_index()

segment_table['% of Total Customers'] = (segment_table['CustomerCount'] / total_customers) * 100
total_revenue = segment_table['TotalRevenue'].sum()
segment_table['% of Total Revenue'] = (segment_table['TotalRevenue'] / total_revenue) * 100

print("--- CUSTOMER SEGMENT TABLE ---")
print(segment_table.to_string(index=False))