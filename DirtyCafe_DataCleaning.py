import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from google.colab import drive
drive.mount('/content/drive')

file_path = '/content/drive/MyDrive/Colab Notebooks/Dirty Cafe Data Cleaning/dirty_cafe_sales.csv'
df = pd.read_csv(file_path)
#import the dirty cafe csv

