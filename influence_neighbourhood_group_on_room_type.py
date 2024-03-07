import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
plt.interactive(False)

listing_df = pd.read_csv('/Users/vittoriasajeva/PycharmProjects/le-wagon-exercises/archive/AB_NYC_2019.csv')

# Let's first list how many room type are available
print(listing_df['room_type'].unique())

# Let's graph the repartition of room types based in the neighbourhood group
sns.countplot(data=listing_df, x='neighbourhood_group', hue='room_type')
plt.show()