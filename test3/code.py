import ee

# Initialize the Earth Engine library
ee.Initialize()

print('Part A -- Creating Layer 1:')
# Variable holding latitude and longitude in Google format
city = ee.Geometry.Point(73.8624, 18.5194)
print(city)

# Printing the point on the map as a point
# Note: Visualization in Python API requires specifying visualization parameters
# For a simple point, we can use Map.addLayer with default parameters
# We'll set the point's color to red for visualization purposes
Map.addLayer(city, {'color': 'FF0000'}, 'City')

print('Part B -- Creating Layer 2:')
start = ee.Date('2016-05-19')
finish = ee.Date('2017-05-19')

# Creating an image collection
imageCollection = ee.ImageCollection("LANDSAT/LC8_L1T_32DAY_NDVI") \
    .filterBounds(city) \
    .filterDate(start, finish) \
    .sort('CLOUD_COVER', False)
print(imageCollection)

# Adding Layer 2 to display Landsat 8 images
# Note: Visualization in Python API can be done using Map.addLayer
# However, displaying an image collection requires specifying visualization parameters
# such as bands and min/max values for visualization
# We'll omit this step for simplicity, but you can customize visualization as needed

# Getting the number of images
count = imageCollection.size()
print(count)

# Adding the image collection to the map
# We won't visualize the image collection directly here as it requires additional parameters
# such as band selection and visualization settings
# You can customize the visualization based on your requirements

# Selecting an image from the image collection
img = ee.Image(imageCollection.sort('CLOUD_COVER').first())
print(img)

# Getting date acquired from properties
date_acquired = img.get('DATE_ACQUIRED')
print(date_acquired.getInfo())  # Getting date from properties
