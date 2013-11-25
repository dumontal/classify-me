# !/usr/bin/python
# coding: utf-8

import sys
sys.path.append('../algorithms')

import unittest
from knn import *

class TestKNN(unittest.TestCase):
	"Unit testing class for KNN algorithm."

	def setUp(self):
		self.knn = KNN()

	def test_2D(self):
		inputs = [[0, 0], [0, 1], [0, 2], [1, 0], [1, 1], [1, 2], [2, 0], [2, 1], [2, 2], [3, 0]]
		outputs = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]

		self.knn.learnFromData(inputs, outputs)	

		prediction = self.knn.predict([[0.5, 0.5]])
		self.assertEqual(prediction[0], 0)

		prediction = self.knn.predict([[2.5, 2.5]])
		self.assertEqual(prediction[0], 1)

if __name__ == '__main__':
    unittest.main()
