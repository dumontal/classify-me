from manage_resources import *
from eval_perf import *
from knn import *

if __name__ == '__main__':
	inputs = loadInputCSV('resources/inputs.csv')
	outputs = loadOutputCSV('resources/outputs.csv')

	block = separateData(inputs, outputs, 0.60)
	trainIn = block['trainIn']
	trainOut = block['trainOut']
	testIn = block['testIn']
	testOut = block['testOut']

	print "Use the K-Nearest Neighbours algorithm for predictions."
	classifier = KNN()
	classifier.learnFromData(trainIn, trainOut)
	prediction = classifier.predict(testIn) # might take a few seconds
	print "Computation done."

	perf = accuracy(prediction, testOut)
	print "Accuracy for randomly distributed data (60% train - 40% test) is of: {0}%".format(perf)
