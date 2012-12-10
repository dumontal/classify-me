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
	"Computes the scalar product between multidimensional vectors x and y"
	if len(x) != len(y):
		print "Woo vectors have differing length!"
		return

	res = 0;
	for k in range(0,len(x)):
		res += x[k] * y[k]
	return sqrt(res)

def max (table):
	"Returns the maximum value of a list of numbers"
	if table == []:
		return
	max = table[0]
	for k in range(1,len(table)):
		if max < table[k]:
			max = table[k]
	return max

def initArray (size, initvalue):
	"Initialize a list with all fields equal to initvalue"
	l = []
	for k in range(0, size):
		l.append(initvalue)
	return l
