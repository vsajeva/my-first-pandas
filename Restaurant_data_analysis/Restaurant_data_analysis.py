# The goal of this challenge is to analyze a restaurant invoices.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips_df = pd.read_csv('/Users/vittoriasajeva/Downloads/le-wagon-exercises/Restaurant_data_analysis/tips.csv')

# Display the 10 first rows of the dataset (no need to sort)
tips_df.head(10)

#How many days per week is the restaurant open?
len(tips_df['day'].unique())

# What day of the week is there more bills?
order = tips_df['day'].value_counts().index
sns.countplot(data=tips_df, x='day', order=order)
plt.show()

# What is the busier time at the restaurant?
order = tips_df['time'].value_counts().index
sns.countplot(data=tips_df, x='time', order=order)
plt.show()

# What day of the week is the more remunerative?
sns.catplot(data=tips_df, x='day', y='total_bill', kind="boxen")
plt.show()


# Does the restaurant earn more over lunches or over dinners ?
sns.catplot(data=tips_df, x='time', y='total_bill', kind="violin")
plt.show()



