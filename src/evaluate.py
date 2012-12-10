# seriously need comments
def precision (predicted, expected):
	N = len(predicted)
	res = float(0)
	for k in range(0, N):
		if (predicted[k] == expected[k]):
			res += 1

	res = res * 100 / float(N)
	return res
