"""
This file contains several python resources used by the KNN algorithm.
It might need some refactoring here in the future.
"""
import math

def isPresent (value, table):
	"Tells if a given value belongs to a given table"
	res = False;
	for k in range(0, len(table)):
		if value == table[k]:
			res = True
	return res

def distance (x, y):
	"Computes the Euclidian distance between multidimensional vectors x and y"
	res = 0;
	for k in range(0,len(x)):
		res += (x[k] - y[k])**2
	return math.sqrt(res)

def mostFrequentLabel (table):
	"Returns the maximum value of a list of numbers"
	label = 0
	for k in range(1,len(table)):
		if table[label] < table[k]:
			label = k
	return label

def initArray (size, initvalue):
	"Initialize a list with all fields equal to initvalue"
	l = []
	for k in range(0, size):
		l.append(initvalue)
	return l
