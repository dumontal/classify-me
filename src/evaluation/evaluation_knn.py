# !/usr/bin/python
# coding: utf-8

import sys
sys.path.append('../algorithms')

from evaluation_utils import *
from knn import *

if __name__ == '__main__':
	pathToInputs = '../../resources/inputs.csv'
	inputs = loadInputCSV(pathToInputs)

	pathToOutputs = '../../resources/outputs.csv'
	outputs = loadOutputCSV(pathToOutputs)

	classifier = KNN()

	"""
	Sample testing with a distribution of 60/40.
	"""

	print "Single testing..."
	block = separateData(inputs, outputs, 0.60)
	trainIn = block['trainIn']
	trainOut = block['trainOut']
	testIn = block['testIn']
	testOut = block['testOut']

	classifier.learnFromData(trainIn, trainOut)
	prediction = classifier.predict(testIn)
	perf = accuracy(prediction, testOut)
	print "Accuracy for randomly distributed data (60% train - 40% test): {0}%".format(perf)

	"""
	Cross validation.
	"""

	print "Cross validation..."
	results = []
	for i in range(0, len(inputs)):
		block = leaveOneOut(inputs, outputs, i)
		trainIn = block['trainIn']
		trainOut = block['trainOut']
		testIn = block['testIn']
		testOut = block['testOut']

		classifier.learnFromData(trainIn, trainOut)
		prediction = classifier.predict(testIn)
		perf = accuracy(prediction, testOut)
		results.append(perf)

	# Compute the average performance of the predictive algorithm.
	perf = statMean(results)
	print "Accuracy over cross validation technique: {0}%".format(perf)
