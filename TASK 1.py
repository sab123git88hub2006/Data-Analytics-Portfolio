# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 00:57:17 2026

@author: sabiya
"""

import pandas as pd

# 1. Load the dataset
df = pd.read_excel('C:\\Users\\shami\\Downloads\\Titanic.xlsx')

# 2. Check for missing values before cleaning
print("Missing values before:")
print(df.isnull().sum())

# 3. Clean the dataset
# Fill missing Age with the average age
df['Age'] = df['Age'].fillna(df['Age'].mean())

# Fill missing Embarked with the most common value ('S')
df['Embarked'] = df['Embarked'].fillna('S')

# Fill missing Cabin with 'Unknown'
df['Cabin'] = df['Cabin'].fillna('Unknown')

# 4. Check missing values again to verify
print("\nMissing values after:")
print(df.isnull().sum())

# 5. Save the cleaned data to a new Excel file
df.to_excel('Titanic_Cleaned.xlsx', index=False)
print("\nDone! Cleaned file saved as 'Titanic_Cleaned.xlsx'")

