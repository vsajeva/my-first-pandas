import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.interactive(False)


listing_df = pd.read_csv('/Users/vittoriasajeva/PycharmProjects/le-wagon-exercises/archive/AB_NYC_2019.csv')

# Sorting neighbourhood listing by ascending oder then filtering the top 10
print(listing_df['neighbourhood'].value_counts().head(10))

# Let's add a barchat with matplotlib
listing_df['neighbourhood'].value_counts().head(10).plot(kind='bar', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()

# Let's use seaborn to do countplot
sns.countplot(data=listing_df, x='neighbourhood_group')
plt.show()

# Sorting the bar of seaborn countplot in ascending order
order = listing_df['neighbourhood_group'].value_counts().index
sns.countplot(data=listing_df, x='neighbourhood_group', order=order)
plt.show()
