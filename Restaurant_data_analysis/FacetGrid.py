import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

tips_df = pd.read_csv('/Users/vittoriasajeva/Downloads/le-wagon-exercises/Restaurant_data_analysis/tips.csv')

# Correlation between the tips and total_bill between smoker and no smoker customers.
with sns.axes_style(style="whitegrid"):
    sns.pairplot(tips_df, height=2, hue="smoker")
    plt.show()

# Linear correlation between the tips and total_bill between smoker and no smoker customers.
with sns.axes_style(style="whitegrid"):
    sns.lmplot(x="total_bill", y="tip", col="smoker", data=tips_df)
    plt.show()