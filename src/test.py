from manage_resources import *
from evaluate import *
from knn import *

if __name__ == '__main__':
	inputs = loadInputCSV('resources/inputs.csv')
	outputs = loadOutputCSV('resources/outputs.csv')

	block = separateData(inputs, outputs, 0.60)
	trainIn = block['trainIn']
	trainOut = block['trainOut']
	testIn = block['testIn']
	testOut = block['testOut']

	classifier = KNN()
	classifier.learnFromData(trainIn, trainOut)
	prediction = classifier.predict(testIn)

	perf = precision(prediction, testOut)
	print perf
