import unittest

def contains_duplicate(arr, distance):
	if len(arr) <= 1:
		return False

	# hash to store the element as key
	# and its index as value
	elem_hash = {}
	for i in xrange(len(arr)):
		# if arr[i] is already in elem_hash
		# compare current index with index from elem_hash
		if arr[i] in elem_hash:
			if (i - elem_hash[arr[i]]) <= distance:
				return True

		# add current element and its index to elem_hash
		# this will override any element to its latest index
		elem_hash[arr[i]] = i

	return False


class TestContainsDuplicate(unittest.TestCase):

	def test_contains_duplicate_1(self):
		given = [1,2,1,3,4,5,6]
		distance = 2
		self.assertTrue(contains_duplicate(given, distance))

	def test_contains_duplicate_2(self):
		given = [1,2,3,1,4,5,6]
		distance = 2
		self.assertFalse(contains_duplicate(given, distance))

	def test_contains_duplicate_3(self):
		given = [1,2,3,4,5,6,1,2,3,1]
		distance = 3
		self.assertTrue(contains_duplicate(given, distance))

	def test_contains_duplicate_4(self):
		given = []
		distance = 2
		self.assertFalse(contains_duplicate(given, distance))

	def test_contains_duplicate_5(self):
		given = [1,2,3,4,5,6]
		distance = 2
		self.assertFalse(contains_duplicate(given, distance))

	def test_contains_duplicate_6(self):
		given = [1]
		distance = 2
		self.assertFalse(contains_duplicate(given, distance))

if __name__ == "__main__":
	unittest.main()