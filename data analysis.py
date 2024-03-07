import pandas as pd

listing_df = pd.read_csv('/Users/vittoriasajeva/PycharmProjects/le-wagon-exercises/archive/AB_NYC_2019.csv')

# Let's check if the columns contained some blank fields
checked_data = listing_df.isnull().sum()
print(checked_data)

# Let's clean the data by removing the columns with blank field
columns_to_drop = ['id', 'host_name', 'last_review']
listing_df.drop(columns_to_drop, axis = 'columns', inplace=True)

# By selecting the reviews_per_month column we can see that some values are NaN (not a number)
print(listing_df['reviews_per_month'])
# Let's provide a default value of 0 to the NaN values in reviews_per_month
listing_df.fillna({'reviews_per_month':0}, inplace = True)
print(listing_df['reviews_per_month'])

# Filtering by rows
print(listing_df[0:5])

# Selecting rows and columns:
print(listing_df [0:10][['name', 'reviews_per_month']])

# Selecting properties with a price inferior to £100
print(listing_df[listing_df['price'] < 100])

# Calculated how many properties are cheaper of £100
print(listing_df[listing_df['price'] < 100].shape)
