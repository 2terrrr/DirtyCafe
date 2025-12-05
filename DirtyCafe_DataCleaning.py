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