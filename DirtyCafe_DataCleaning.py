!pip install ydata-profiling
from ydata_profiling import ProfileReport

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from google.colab import drive
drive.mount('/content/drive')

file_path = '/content/drive/MyDrive/Colab Notebooks/Dirty Cafe Data Cleaning/dirty_cafe_sales.csv'
df = pd.read_csv(file_path)

profile = ProfileReport(df, title="Dirty Cafe Sales Report", explorative=True)

display(profile.to_notebook_iframe())

from google.colab import data_table
data_table.enable_dataframe_formatter()

cleaning = ["ERROR", "UNKNOWN", "Missing value", "nan", "missing value", "", " "]
df = df.replace(cleaning, np.nan)

df = df.astype({'Payment Method': str, 'Location': str})


df["Quantity"] = pd.to_numeric(df["Quantity"], errors='coerce')
df["Price Per Unit"] = pd.to_numeric(df["Price Per Unit"], errors='coerce')
df["Total Spent"] = pd.to_numeric(df["Total Spent"], errors='coerce')
df["Transaction Date"] = pd.to_datetime(df['Transaction Date'], errors='coerce')

mean_prices = df.dropna(subset=["Price Per Unit"]).groupby("Item")["Price Per Unit"].mean()
print(mean_prices)

def missing(df):
  price_change = {'Cake': 3.00, 'Coffee': 2.00, 'Cookie': 1.00, 'Juice': 3.00, 'Pastry': 2.50, 'Salad': 5.00, 'Sandwich': 4.00, 'Smoothie': 4.00, 'Tea': 1.50}
  def fill(row):
    item = row['Item']
    price = row['Price Per Unit']

    if item in price_change:
      if pd.isna(price):
        return price_change[item]
      else:
        return price
    return price

  df['Price Per Unit'] = df.apply(fill, axis=1)
  return df

missing(df)

df["Total Spent"] = df["Quantity"] * df["Price Per Unit"]

df = df.dropna(subset=['Quantity', 'Price Per Unit']).copy()

profile = ProfileReport(df, title="Dirty Cafe Sales Report", explorative=True)

display(profile.to_notebook_iframe())