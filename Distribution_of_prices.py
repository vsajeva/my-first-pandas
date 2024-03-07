import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.interactive(False)

listing_df = pd.read_csv('/Users/vittoriasajeva/PycharmProjects/le-wagon-exercises/archive/AB_NYC_2019.csv')

# Let's look at the distribution of the price against the listings
sns.displot(listing_df['price'])
plt.show()

# Let's filter properties that are over $500 per night.
# This will tell me how many properties I can discard from my analysis as their listing are not too representative.
print(listing_df[listing_df['price'] > 500].shape)

# Let's now consider the distribution of the most common properties that are up to $500 per night
affordable_df = listing_df[listing_df['price'] <= 500]
sns.distplot(affordable_df['price'])
plt.show()

# Mean estrapolation
print(affordable_df['price'].mean())
