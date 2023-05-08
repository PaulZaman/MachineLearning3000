# imports

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Creating the two datasets
data_x: pd.DataFrame = pd.read_csv('data/Data_X.csv')
data_y: pd.DataFrame = pd.read_csv('data/Data_Y.csv')

# remove the empty cells
data_x = data_x.dropna()

from sklearn.preprocessing import OneHotEncoder

# Select the column to encode
col = ['COUNTRY']
# Create the encoder
encoder = OneHotEncoder()
# Fit the encoder
encoder.fit(data_x[col])
# Transform the column
encoded = encoder.transform(data_x[col]).toarray()
# Create the new columns
for i, category in enumerate(encoder.categories_[0]):
    data_x[category] = encoded[:, i]
# Drop the old column
data_x = data_x.drop(columns=col)

# Select the numerical columns to normalize
cols = [col for col in data_x.columns if col not in ['ID', 'DAY_ID', 'FR', 'DE']]
# Normalize the data
data_x[cols] = (data_x[cols] - data_x[cols].mean()) / data_x[cols].std()

# remove the lines from the data_y dataset
data_y = data_y[data_y['ID'].isin(data_x['ID'])]

# merge the two datasets
data_x = data_x.merge(data_y, on='ID')


# save the data
data_x.to_csv('data/Data_X_clean_normalized.csv', index=False)


