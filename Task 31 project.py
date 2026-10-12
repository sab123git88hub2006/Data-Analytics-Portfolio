# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 20:09:58 2026

@author: shami
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


columns_to_use = ['show_id', 'title', 'release_year', 'rating', 'duration', 
                  'listed_in', 'type']
df = pd.read_excel('C:\\Users\\shami\\Downloads\\netflix_titles_nov_2019.xlsx'
                   , usecols=columns_to_use)
df['rating'] = df['rating'].fillna('UR')
df['primary_genre'] = df['listed_in'].apply(lambda x: str(x).split(',')[0].strip())
def extract_duration(row):
    try:
        return float(str(row['duration']).split(' ')[0])
    except:
        return np.nan

df['duration_num'] = df.apply(extract_duration, axis=1)
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.alpha'] = 0.3
plt.figure(figsize=(6, 4))
type_counts = df['type'].value_counts()
plt.bar(type_counts.index, type_counts.values, color=['#1f77b4', '#ff7f0e'])
plt.title('1. Content Type Breakdown (Movies vs TV Shows)')
plt.ylabel('Total Catalog Titles')
plt.tight_layout()
plt.savefig('viz1_content_type.png')
plt.show()


plt.figure(figsize=(8, 4))
top_genres = df['primary_genre'].value_counts().head(10)
plt.barh(top_genres.index[::-1], top_genres.values[::-1], color='#2ca02c')
plt.title('2. Top 10 Catalog Genres')
plt.xlabel('Number of Titles')
plt.tight_layout()
plt.savefig('viz2_top_genres.png')
plt.show()

df_filtered = df[df['release_year'] >= 2010]
trend_data = df_filtered.groupby(['release_year', 'type']).size().unstack(fill_value=0)

plt.figure(figsize=(8, 4))
plt.plot(trend_data.index, trend_data['Movie'], label='Movies', marker='o', color='#d62728')
plt.plot(trend_data.index, trend_data['TV Show'], label='TV Shows', marker='s', color='#9467bd')
plt.title('3. Content Release Trend by Year (2010-Present)')
plt.xlabel('Release Year')
plt.ylabel('Number of Titles Released')
plt.legend()
plt.tight_layout()
plt.savefig('viz3_release_trend.png')
plt.show()

plt.figure(figsize=(8, 4))
top_ratings = df['rating'].value_counts().head(7)
plt.bar(top_ratings.index, top_ratings.values, color='#e377c2')
plt.title('4. Maturity Rating Distribution')
plt.ylabel('Title Count')
plt.tight_layout()
plt.savefig('viz4_ratings.png')
plt.show()

plt.figure(figsize=(8, 4))
movies_df = df[df['type'] == 'Movie'].dropna(subset=['duration_num'])
plt.hist(movies_df['duration_num'], bins=30, color='#17becf', edgecolor='black')
plt.axvline(movies_df['duration_num'].median(), color='red', linestyle='dashed', 
            label=f"Median: {int(movies_df['duration_num'].median())} mins")
plt.title('5. Movie Runtime Distribution')
plt.xlabel('Duration (Minutes)')
plt.ylabel('Number of Movies')
plt.legend()
plt.tight_layout()
plt.savefig('viz5_movie_duration.png')
plt.show()

plt.figure(figsize=(8, 4))
tv_df = df[df['type'] == 'TV Show'].dropna(subset=['duration_num'])
tv_counts = tv_df['duration_num'].value_counts().sort_index().head(6)
plt.bar(tv_counts.index.astype(int).astype(str) + ' Season(s)', tv_counts.values, color='#bcbd22')
plt.title('6. TV Show Season Count Distribution')
plt.xlabel('Number of Seasons')
plt.ylabel('Title Count')
plt.tight_layout()
plt.savefig('viz6_tv_duration.png')
plt.show()