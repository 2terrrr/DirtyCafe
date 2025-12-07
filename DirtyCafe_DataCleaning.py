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