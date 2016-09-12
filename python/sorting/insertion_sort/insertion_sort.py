import unittest

def insertion_sort(nums):
	length = len(nums)
	for i in range(1, length):
		j = i
		while nums[j] < nums[j-1] and j>0:
			nums[j], nums[j-1] = nums[j-1], nums[j]
			j = j-1

	return nums


class TestInsertionSort(unittest.TestCase):

	def test_insertion_sort_1(self):
		given = [2,4,3,1,5]
		expected = [1,2,3,4,5]
		self.assertEqual(expected, insertion_sort(given))

	def test_insertion_sort_2(self):
		given = [5,4,3,2,1]
		expected = [1,2,3,4,5]
		self.assertEqual(expected, insertion_sort(given))

	def test_insertion_sort_3(self):
		given = [2,7,4,1,5,3]
		expected = [1,2,3,4,5,7]
		self.assertEqual(expected, insertion_sort(given))

	def test_insertion_sort_4(self):
		given = [2]
		expected = [2]
		self.assertEqual(expected, insertion_sort(given))

	def test_insertion_sort_5(self):
		given = []
		expected = []
		self.assertEqual(expected, insertion_sort(given))

	def test_insertion_sort_6(self):
		given = [1,3,5,7,9,10]
		expected = [1,3,5,7,9,10]
		self.assertEqual(expected, insertion_sort(given))


if __name__ == "__main__":
	unittest.main()