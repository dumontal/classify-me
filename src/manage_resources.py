import csv
import random

def loadInputCSV (filename):
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
	f = open(filename, 'rb')
	reader = csv.reader(f)
	l = []
	for row in reader:
		l.append(int(row[0]))
	return l

def separateData(inputs, outputs, rate):
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
