import csv
import random

def loadInputCSV (filename):
	"Loads a CSV as a list of floats."
	f = open(filename, 'rb')
	reader = csv.reader(f)
	l = []
	for row in reader:
		tmp = []
		for e in row:
			tmp.append(float(e))
		l.append(tmp)
	return l

def loadOutputCSV (filename):
	"Loads a CSV as a list of integers."
	f = open(filename, 'rb')
	reader = csv.reader(f)
	l = []
	for row in reader:
		l.append(int(row[0]))
	return l

def separateData(inputs, outputs, rate):
	"Performs a random distribution of data over training and testing. Use a randomly generated variable to do so."
	# rate = proportion of the initial data used for training.
	trainIn = []
	trainOut = []
	testIn = []
	testOut = []

	for i in range(0, len(inputs)):
		r = random.random()
		if (r < rate):
			trainIn.append(inputs[i])
			trainOut.append(outputs[i])
		else:
			testIn.append(inputs[i])
			testOut.append(outputs[i])

	block = {'trainIn': trainIn, 'trainOut': trainOut, 'testIn': testIn, 'testOut': testOut}
	return block

def leaveOneOut(inputs, outputs, rowToExclude):
	"Splits original data so that only one row is tested. Useful for cross validation techniques."
	trainIn = []
	trainOut = []
	testIn = []
	testOut = []

	for i in range(0, len(inputs)):
		if (i != rowToExclude):
			trainIn.append(inputs[i])
			trainOut.append(outputs[i])
		else:
			testIn.append(inputs[i])
			testOut.append(outputs[i])

	block = {'trainIn': trainIn, 'trainOut': trainOut, 'testIn': testIn, 'testOut': testOut}
	return block