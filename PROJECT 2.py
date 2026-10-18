import pandas as pd

df = pd.read_csv("C:\\Users\\shami\\Downloads\\owid-covid-data.csv")

# 2. Drop rows where essential identifiers are missing
df = df.dropna(subset=['iso_code', 'location', 'date'])

# 3. Handle missing values for daily cases and deaths (assume 0 where data is missing)
df['new_cases'] = df['new_cases'].fillna(0)
df['new_deaths'] = df['new_deaths'].fillna(0)
df['total_cases'] = df['total_cases'].fillna(0)
df['total_deaths'] = df['total_deaths'].fillna(0)

# 4. Filter out global or regional aggregate rows (e.g., 'World', 'Europe') for country-level analysis
aggregates = [
    'World', 'International', 'High income', 'Upper middle income', 
    'Lower middle income', 'Low income', 'Europe', 'North America', 
    'Asia', 'European Union', 'South America', 'Africa', 'Oceania'
]
df_countries = df[~df['location'].isin(aggregates)].copy()

# 5. Calculate Case Fatality Rate (CFR) directly in Python so you don't need a formula in Power BI!
df_countries['case_fatality_rate'] = (df_countries['total_deaths'] / df_countries['total_cases']) * 100
df_countries['case_fatality_rate'] = df_countries['case_fatality_rate'].fillna(0)

# 6. Save as a CSV file as requested
output_filename = "C:\\Users\\shami\\OneDrive\\Desktop\\SABIYA\\cleaned_covid_data.csv"
df_countries.to_csv(output_filename, index=False)

print(f"Dataset successfully cleaned and saved as '{output_filename}'!")