import urllib.request
import pandas as pd
import matplotlib.pyplot as plt
plt.interactive(False)

from PIL import Image
from io import BytesIO

listing_df = pd.read_csv('/Users/vittoriasajeva/PycharmProjects/le-wagon-exercises/archive/AB_NYC_2019.csv')

# Display of the geographic position of the most affordable properties.
# The distribution of the data proves that the most expensive properties are in Manhattan.
affordable_df = listing_df[listing_df['price'] <= 500]

# Fetch the New York City map image
url = "https://upload.wikimedia.org/wikipedia/commons/e/ec/Neighbourhoods_New_York_City_Map.PNG"
response = urllib.request.urlopen(url)
img_data = response.read()

# Open image using PIL
img = Image.open(BytesIO(img_data))

# Display the New York City map
plt.imshow(img, zorder=0, extent=[-74.258, -73.7, 40.49, 40.92])
ax = plt.gca()

# Plot affordable listings on the map
affordable_df.plot (ax = ax, zorder=1, kind='scatter', x='longitude', y='latitude', c="price", cmap='inferno', colorbar=True, alpha=0.8,figsize=(12,8))
plt.show()