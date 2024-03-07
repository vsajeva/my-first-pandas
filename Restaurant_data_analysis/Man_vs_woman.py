# The goal of this challenge is to analyze a restaurant invoices.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips_df = pd.read_csv('/Users/vittoriasajeva/Downloads/le-wagon-exercises/Restaurant_data_analysis/tips.csv')

# Does man tip more than woman?
sns.catplot(data=tips_df, x='sex', y='tip', kind="bar")
plt.show()

# Who spend more men or woman?
sns.catplot(data=tips_df, x='sex', y='total_bill', kind="bar")
plt.show()