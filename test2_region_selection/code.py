import ee

# Authenticating to Earth Engine servers
ee.Authenticate()
ee.Initialize()

# Define point of interest
point = ee.Geometry.Point(-122.27, 37.88)

# Center the map on a specific location
Map.centerObject(ee.Geometry.Point(-122.3764, 37.6277), 12)

# Define Landsat bands
bands = ['B2', 'B3', 'B4', 'B5', 'B6', 'B7']

# Filter and select the first image with least cloud cover
image = ee.Image(ee.ImageCollection('LANDSAT/LC08/C01/T1_TOA')
                 .filterBounds(point)
                 .sort('CLOUD_COVER')
                 .first()) \
    .select(bands)

# Print the image
print(image)

# Add the image to the map
Map.addLayer(image, {'bands': ['B4', 'B3', 'B2'], 'max': 0.3}, 'image')

# Define regions of interest (bare, water, vegetation)
bare = ee.Geometry.Rectangle(...)
water = ee.Geometry.Rectangle(...)
vegetation = ee.Geometry.Rectangle(...)

# Calculate mean values for each region
bearMean = image.reduceRegion(reducer=ee.Reducer.mean(), geometry=bare, scale=10).values()
waterMean = image.reduceRegion(reducer=ee.Reducer.mean(), geometry=water, scale=10).values()
vegetationMean = image.reduceRegion(reducer=ee.Reducer.mean(), geometry=vegetation, scale=10).values()

# Print mean values
print('Bear:', bearMean.getInfo())
print('Vegetation:', vegetationMean.getInfo())
print('Water:', waterMean.getInfo())

# Define chart labels
labels = ['bear', 'vegetation', 'water']

# Create chart
chart = ui.Chart.image.regions(image, ee.FeatureCollection([
    ee.Feature(bare, {'label': 'bear'}),
    ee.Feature(vegetation, {'label': 'vegetation'}),
    ee.Feature(water, {'label': 'water'})]),
    reducer=ee.Reducer.mean(), scale=10, xProperty='label', bands=bands)

# Print the chart
print(chart)

# Collect endmembers
endmembers = ee.Array.cat([bearMean, vegetationMean, waterMean], 1)

# Convert image to array
arrayImage = image.toArray().toArray(1)

# Solve for unmixed fractions
unmixed = ee.Image(endmembers).matrixSolve(arrayImage)

# Reshape unmixed fractions to image
unmixedImage = unmixed.arrayProject([0]).arrayFlatten([['bare', 'veg', 'water']])

# Add unmixed fractions to the map
Map.addLayer(unmixedImage, {}, 'fractions')

# Display the map
Map
