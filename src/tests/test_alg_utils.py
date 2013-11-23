# !/usr/bin/python
# coding: utf-8

import sys
sys.path.append('../algorithms')

import unittest
from alg_utils import *

class TestAlgUtils(unittest.TestCase):
	"Unit testing class for alg_utils.py package."

	def test_isPresent_valid(self):
		value = 4
		table = [1, 2, 3, 4, 5, 6]
		present = isPresent(value, table)
		self.assertEqual(present, True)

	def test_isPresent_invalid(self):
		value = 0
		table = [1, 2, 3, 4, 5, 6]
		present = isPresent(value, table)
		self.assertEqual(present, False)

	def test_distance_1D(self):
		x = [0]
		y = [2]
		dist = distance(x, y)
		self.assertEqual(dist, 2)

	def test_distance_2D(self):
		x = [0, 0]
		y = [3, 4]
		dist = distance(x, y)
		self.assertEqual(dist, 5)

	def test_distance_7D(self):
		x = [0, 0, 0, 0, 0, 0, 0]
		y = [2, 2, 2, 2, 2, 2, 1]
		dist = distance(x, y)
		self.assertEqual(dist, 5)

	def test_mostFrequentLabel(self):
		values = [10, 136, 96, 365, 42, 366]
		label = mostFrequentLabel(values)
		self.assertEqual(label, 5)

	def test_initArray(self):
		size = 1000
		val = 2
		table = initArray(size, val)
		for i in range(0, size):
			self.assertEqual(table[i], val)

if __name__ == '__main__':
    unittest.main()
