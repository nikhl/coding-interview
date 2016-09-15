from random import randint

def fisher_yates_shuffle(arr):
	if len(arr) <= 1:
		return arr

	length = len(arr)

	# if we run loop length-1(0..length-2) times
	# all the elements are considered for shuffling
	for i in xrange(length-2):
		j = randint(i,(length-1))

		# swap elements at i and j indices
		arr[i], arr[j] = arr[j], arr[i]

	return arr


if __name__ == "__main__":
	print fisher_yates_shuffle([1,2,3,4,5,6,7])
	print fisher_yates_shuffle([1,2,3])
	print fisher_yates_shuffle([1])
	print fisher_yates_shuffle([3,1,6,99,37,34,22,59])