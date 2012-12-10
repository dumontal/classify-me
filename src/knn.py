import knn-utils;

class KNN (object):
	"Implementation of the K-Nearest Neighbours algorithm"


	def learnFromData(self, inputs, outputs):
		"The learning step here only consists in storing the inputs and the corresponding outputs"
		# Note: We should use cross validation to find the "best" K and the number of labels

		if len(inputs) != len(outputs):
			print "Woo the learning data is inconsistent!"
			return
		self.inputs = inputs
		self.outputs = outputs
		self.K = 10
		self.noLabels = 2


	def predict(self, inputs, parameters):
		"Use the parameters learned from the above method to predict the labels"
		
		K = self.K
		trainIn = self.inputs
		trainOut = self.outputs
		noLabels = self.noLabels
		res = []

		print "Applying the K-Nearest Neighbours algorithm to assign a label to each raw data..."
		#iterate on every testing row
		for n in range(0, len(inputs)): 

			# number of neighbours with corresponding label
			labelArray = initArray(noLabels, 0)
			# number of neighbours actually found
			cpt = 0
			# indexes of already found neighbours
			indexesAlreadyChecked = initArray(K, -1)
			
			while (cpt < K):
				minDistance = -1
				minIndex = -1
				# browse all the possible neighbours
				for index in range(0, len(trainIn)):
					# do not count the same row twice
					if isPresent(index, indexesAlreadyChecked) == False:
						
						dist = distance(inputs[n], trainIn[index])
						if (minDistance == -1) || (dist < minDistance):
							minDistance = dist
							minIndex = index

				# We have found the cpt-th neighbour! Congratulations!
				indexesAlreadyChecked[cpt] = minIndex
				cpt += 1
				labelArray[trainOut[minIndex]] += 1 # population increases

			# Now decide which label to give to the testing input (ie the most populous)
			label = max(labelArray)
			res.append(label)

		print "Computation done."
		return res
