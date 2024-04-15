import ee

# Initialize the Earth Engine library
ee.Initialize()

# Define the Landsat collection
landsatCollection = ee.ImageCollection('LANDSAT/LC08/C01/T1').filterDate('2017-01-01', '2017-12-31')

# Make a cloud-free composite
composite = ee.Algorithms.Landsat.simpleComposite(landsatCollection, asFloat=True)

# Merge the geometry layers into a single FeatureCollection
newfc = urban.merge(vegetation).merge(water).merge(urban).merge(fields)

# Define bands for classification
bands = ['B2', 'B3', 'B4', 'B5', 'B6', 'B7']

# The name of the property on the points storing the class label
classProperty = 'landcover'

# Sample the composite to generate training data
training = composite.select(bands).sampleRegions(collection=newfc, properties=[classProperty], scale=30)

# Train a CART classifier
classifier = ee.Classifier.cart().train(features=training, classProperty=classProperty)

# Print some info about the classifier (specific to CART)
print('CART, explained', classifier.explain())

# Classify the composite
classified = composite.classify(classifier)

# Add classified layer to the map
Map.centerObject(newfc)
Map.addLayer(classified, {'min': 0, 'max': 3, 'palette': ['red', 'blue', 'green', 'yellow']})

# Add a column of random uniforms to the training dataset
withRandom = training.randomColumn('random')

# Reserve some of the data for testing
split = 0.7  # Roughly 70% training, 30% testing
trainingPartition = withRandom.filter(ee.Filter.lt('random', split))
testingPartition = withRandom.filter(ee.Filter.gte('random', split))

# Train the classifier with 70% of the data
trainedClassifier = ee.Classifier.gmoMaxEnt().train(features=trainingPartition, classProperty=classProperty, inputProperties=bands)

# Classify the test FeatureCollection
test = testingPartition.classify(trainedClassifier)

# Print the confusion matrix
confusionMatrix = test.errorMatrix(classProperty, 'classification')
print('Confusion Matrix', confusionMatrix)
