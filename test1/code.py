import ee

# Initialize the Earth Engine library.
ee.Initialize()

# Define the region of interest (roi3).
roi3 = ee.Geometry.Point(-122.4439, 37.7538).buffer(500)

# Load Landsat 8 TOA images, get the least cloudy 2015 image.
image = ee.Image(ee.ImageCollection('LANDSAT/LC08/C01/T1_TOA')
    # Geographically filter.
    .filterBounds(roi3)
    # Filter to get only 2015.
    .filterDate('2015-01-01', '2015-12-31')
    # Sort by cloud cover metadata (ascending).
    .sort('CLOUD_COVER')
    # Get the least cloudy image.
    .first())

# Display the input imagery.
Map.centerObject(roi3, 11)
Map.addLayer(image, {'bands': ['B4', 'B3', 'B2'], 'max': 0.3}, 'Landsat image')

# Merge the hand-drawn features into a single FeatureCollection.
newfc = bare.merge(vegetation).merge(water).merge(houses)

# Use these bands in the prediction.
bands = ['B2', 'B3', 'B4', 'B5', 'B6', 'B7']

# Make training data by 'overlaying' the points on the image.
training = image.select(bands).sampleRegions(**{
  'collection': newfc, 
  'properties': ['landcover'], 
  'scale': 10
})

# Get a CART classifier and train it.
classifier = ee.Classifier.cart().train(**{
  'features': training, 
  'classProperty': 'landcover', 
  'inputProperties': bands
})

# Classify the image.
classified = image.select(bands).classify(classifier)

# Display the classification results.
Map.addLayer(classified, {'min': 0, 'max': 2, 'palette': ['red', 'green', 'blue', 'yellow']}, 'classification')
