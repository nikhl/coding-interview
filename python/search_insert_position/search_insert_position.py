import unittest

def search_insert_pos(arr, key):
	# if arr is empty, return 0
	if not arr:
		return 0

	start = 0
	end = len(arr)-1

	while start <= end:
		mid = (start+end)/2

		# if key is found in arr, return its index
		if arr[mid] == key:
			return mid

		if arr[mid] < key:
			start = mid + 1
		else:
			end = mid - 1

	# if start is still with in array index
	if start < len(arr):
		# if key falls in between mid and start
		if arr[mid] < key and arr[start] >= key:
			return mid + 1

	# if start is out of array index i.e mid points to last
	# element in array
	if arr[mid] < key:
		return mid + 1

	return mid



class TestSearchInsertPosition(unittest.TestCase):

	def test_search_insert_1(self):
		given = [1,3,5,6]
		key = 5
		index = 2
		self.assertEqual(index, search_insert_pos(given, key))

	def test_search_insert_2(self):
		given = [1,3,5,6]
		key = 2
		index = 1
		self.assertEqual(index, search_insert_pos(given, key))

	def test_search_insert_3(self):
		given = [1,3,5,6]
		key = 7
		index = 4
		self.assertEqual(index, search_insert_pos(given, key))

	def test_search_insert_4(self):
		given = [1,3,5,6]
		key = 4
		index = 2
		self.assertEqual(index, search_insert_pos(given, key))

	def test_search_insert_5(self):
		given = []
		key = 4
		index = 0
		self.assertEqual(index, search_insert_pos(given, key))

	def test_search_insert_6(self):
		given = [3]
		key = 2
		index = 0
		self.assertEqual(index, search_insert_pos(given, key))

	def test_search_insert_7(self):
		given = [3]
		key = 4
		index = 1
		self.assertEqual(index, search_insert_pos(given, key))


if __name__ == "__main__":
	unittest.main()