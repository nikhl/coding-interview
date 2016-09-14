import unittest

def contains_duplicate(arr):
	if len(arr) <= 1:
		return False

	elements = set()
	for i in arr:
		if i in elements:
			return True

		elements.add(i)

	return False

class TestContainsDuplicate(unittest.TestCase):

	def test_contains_duplicate_1(self):
		given = [1,2,3,4,5,6,1]
		self.assertTrue(contains_duplicate(given))

	def test_contains_duplicate_2(self):
		given = [1,2,3,4,5,6]
		self.assertFalse(contains_duplicate(given))

	def test_contains_duplicate_3(self):
		given = []
		self.assertFalse(contains_duplicate(given))

	def test_contains_duplicate_4(self):
		given = [1]
		self.assertFalse(contains_duplicate(given))

	def test_contains_duplicate_5(self):
		given = [1,1]
		self.assertTrue(contains_duplicate(given))

if __name__ == "__main__":
	unittest.main()