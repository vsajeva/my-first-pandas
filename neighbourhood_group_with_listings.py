import pandas as pd

listing_df = pd.read_csv('/Users/vittoriasajeva/PycharmProjects/le-wagon-exercises/archive/AB_NYC_2019.csv')

# Filter by neighbourhood_group
print(listing_df['neighbourhood_group'].unique())

# Number of listings for neighbourhood_group
print(listing_df['neighbourhood_group'].value_counts())