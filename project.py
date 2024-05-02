import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from functionssmoking import *

dataset = pd.read_csv('C:/Users/ABDURAHMAN BEY/PycharmProjects/specialTopicsProject/smoking_health_data_final.csv')
dataset.drop(dataset.columns[4], axis=1, inplace=True)
dataset.dropna(how='any', inplace=True, axis=0)
a = "serkan"
print("Number of samples: ", len(dataset))

df_sorted_heart_rate = dataset.sort_values(by='heart_rate')
dataset = drop_outliers(df_sorted_heart_rate, 'heart_rate')

print(dataset)

df_sorted_chol = dataset.sort_values(by='chol')
dataset = drop_outliers(df_sorted_chol, 'chol')

print(dataset)

#plt.hist(dataset_filtered['age'], dataset_filtered['chol'])