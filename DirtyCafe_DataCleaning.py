import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

file_path = '/content/drive/MyDrive/Colab Notebooks/Dirty Cafe Data Cleaning/dirty_cafe_sales.csv'
df = pd.read_csv(file_path)
#import the dirty cafe csv

from google.colab import data_table
data_table.enable_dataframe_formatter()

df_cleaned
#to see the dataset using colabs table feature

df = df.astype({'Payment Method': str, 'Location': str})

df["Quantity"] = pd.to_numeric(df["Quantity"], errors='coerce')
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors='coerce')
df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors='coerce')
df["Transaction Date"] = pd.to_datetime(df['Transaction Date'], errors='coerce')

dirty_labels = ["ERROR", "UNKNOWN", "Missing value", "missing value", "nan", "", " "]
df = df.replace(dirty_labels, np.nan)

standard_prices = {
    "Cake": 3.0,
    "Coffee": 2.0,
    "Cookie": 1.0,
    "Juice": 3.0,
    "Salad": 5.0,
    "Sandwich": 4.0,
    "Smoothie": 4.0,
    "Tea": 1.5
}

# 1. Fill missing 'Price Per Unit' based on the Item name
for item, price in standard_prices.items():
    # Find rows where Item matches but Price is missing, and fill it
    mask = (df['Item'] == item) & (df['Price Per Unit'].isna())
    df.loc[mask, 'Price Per Unit'] = price