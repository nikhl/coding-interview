import unittest


def max_heapify(arr, idx, heap_length):
	left_idx = (2*idx)+1
	right_idx = (2*idx)+2

	# if both left and right child needs to be considered
	if (left_idx<=heap_length) and (right_idx<=heap_length):
		# pick max among left and right child and swap
		# if parent is less than max among children
		if arr[left_idx] < arr[right_idx]:
			if arr[idx] < arr[right_idx]:
				arr[right_idx], arr[idx] = arr[idx], arr[right_idx]
				max_heapify(arr, right_idx, heap_length)
		
		# if left child is max among children and parent
		# is less than left child
		if arr[idx] < arr[left_idx]:
			arr[left_idx], arr[idx] = arr[idx], arr[left_idx]
			max_heapify(arr, left_idx, heap_length)

	#if only left child exist or needs to be considered
	if left_idx <= heap_length:
		if arr[idx] < arr[left_idx]:
			arr[left_idx], arr[idx] = arr[idx], arr[left_idx]
			max_heapify(arr, left_idx, heap_length)		


def heap_sort(arr):
	# if heap_length <= 1, array is already sorted
	heap_length = len(arr)
	if heap_length <= 1:
		return arr

	# reduce heap_length by 1 to match with array indices
	# as array indices start with 0
	heap_length -= 1

	# heapify the given arr, after this step, max element
	# will be located at index 0
	for i in xrange((heap_length/2), -1, -1):
		max_heapify(arr, i, heap_length)

	while heap_length > 0:
		# interchange max element with last element
		# and reduce heap_length by 1
		# heapify again to bring next max element to index 0
		arr[0], arr[heap_length] = arr[heap_length], arr[0]
		heap_length -= 1
		max_heapify(arr, 0, heap_length)

	return arr

	

class TestHeapSort(unittest.TestCase):

	def test_heap_sort_1(self):
		given = [2,4,3,1,5]
		expected = [1,2,3,4,5]
		self.assertEqual(expected, heap_sort(given))

	def test_heap_sort_2(self):
		given = [5,4,3,2,1]
		expected = [1,2,3,4,5]
		self.assertEqual(expected, heap_sort(given))

	def test_heap_sort_3(self):
		given = [2,7,4,1,5,3]
		expected = [1,2,3,4,5,7]
		self.assertEqual(expected, heap_sort(given))

	def test_heap_sort_4(self):
		given = [2]
		expected = [2]
		self.assertEqual(expected, heap_sort(given))

	def test_heap_sort_5(self):
		given = []
		expected = []
		self.assertEqual(expected, heap_sort(given))

	def test_heap_sort_6(self):
		given = [1,3,5,7,9,10]
		expected = [1,3,5,7,9,10]
		self.assertEqual(expected, heap_sort(given))


if __name__ == "__main__":
	unittest.main()