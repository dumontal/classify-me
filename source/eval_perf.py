# This file contains several "evaluator" functions

def accuracy (predicted, expected):
	"Compares the accuracy of the predicted vector related to the expected vector. Returns a percentage value."
	N = len(predicted)
	res = float(0)
	for k in range(0, N):
		if (predicted[k] == expected[k]):
			res += 1

	res = res * 100 / float(N)
	res = round(res, 2)
	return res
