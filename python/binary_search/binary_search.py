import unittest

def binary_search(arr, key):

	start = 0
	end = len(arr)-1

	while start<=end:
		mid = (start+end)/2

		if arr[mid]==key:
			return mid
		elif arr[mid] > key:
			end = mid-1
		else:
			start = mid+1

	# return -1 indicating element not found
	return -1


class TestBinarySearch(unittest.TestCase):

	def test_binary_search_1(self):
		arr = [1,2,3,4,5,6,7]
		key = 1
		index = 0
		self.assertEqual(index, binary_search(arr, key))

	def test_binary_search_2(self):
		arr = []
		key = 10
		index = -1
		self.assertEqual(index, binary_search(arr, key))

	def test_binary_search_3(self):
		arr = [1,2,3,4,5,6,7]
		key = 6
		index = 5
		self.assertEqual(index, binary_search(arr, key))

	def test_binary_search_4(self):
		arr = [1,2,3,4,5,6,7]
		key = 7
		index = 6
		self.assertEqual(index, binary_search(arr, key))

	def test_binary_search_5(self):
		arr = [1]
		key = 7
		index = -1
		self.assertEqual(index, binary_search(arr, key))

	def test_binary_search_6(self):
		arr = [10]
		key = 10
		index = 0
		self.assertEqual(index, binary_search(arr, key))

	def test_binary_search_7(self):
		arr = [1,2]
		key = 2
		index = 1
		self.assertEqual(index, binary_search(arr, key))

	def test_binary_search_8(self):
		arr = [10,20,30]
		key = 20
		index = 1
		self.assertEqual(index, binary_search(arr, key))

	def test_binary_search_9(self):
		arr = [1,2,3,4,5,6,7]
		key = 2
		index = 1
		self.assertEqual(index, binary_search(arr, key))

# You can run all testcases by navigating to this directory
# and run "python binary_search.py"
if __name__ == "__main__":
	unittest.main()
