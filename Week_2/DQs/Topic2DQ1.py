import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Example dataset loading
df = pd.read_csv('C:/Users/khbil/Documents/GCU/DSC-510/Week_2/dog_breeds.csv')

df['height'] = (df['max_height_male'] + df['max_height_female'])/2

z_scores = np.abs(stats.zscore(df['height']))
outliers_z = df[z_scores > 3]

# Identify outliers using IQR
Q1, Q3 = np.percentile(df['height'], [25, 75])
IQR = Q3 - Q1
outliers_iqr = df[(df['height'] < (Q1 - 1.5 * IQR)) | (df['height'] > (Q3 + 1.5 * IQR))]

# Visualization with boxplot
sns.boxplot(x=df['height'])
plt.title('Height Distribution with Outliers')
plt.xlabel('Height (in)')
plt.show()
