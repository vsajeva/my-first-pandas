# The goal of this challenge is to analyze a restaurant invoices.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips_df = pd.read_csv('/Users/vittoriasajeva/Downloads/le-wagon-exercises/Restaurant_data_analysis/tips.csv')

# Do most of the customer smoke?
order = tips_df['smoker'].value_counts().index
sns.countplot(data=tips_df, x='smoker', order=order)
plt.show()

# Who spend more smoker or no-smoker customer?
sns.catplot(data=tips_df, x='smoker', y='total_bill', kind="box")
plt.show()

# Distribution of the average customer smoker/no-smoker spending over time.
g = sns.FacetGrid(tips_df, col="time", row="smoker")
g.map(plt.hist, "total_bill")
plt.show()