import unittest

def selection_sort(nums):
	l = len(nums)
	for i in range(l-1):
		for j in range(i+1, l):
			if nums[i] > nums[j]:
				nums[i], nums[j] = nums[j], nums[i]
	return nums

class TestSelectionSort(unittest.TestCase):

	def test_selection_sort_1(self):
		given = [2,4,3,1,5]
		expected = [1,2,3,4,5]
		self.assertEqual(expected, selection_sort(given))

	def test_selection_sort_2(self):
		given = [5,4,3,2,1]
		expected = [1,2,3,4,5]
		self.assertEqual(expected, selection_sort(given))

	def test_selection_sort_3(self):
		given = [2,7,4,1,5,3]
		expected = [1,2,3,4,5,7]
		self.assertEqual(expected, selection_sort(given))

	def test_selection_sort_4(self):
		given = [2]
		expected = [2]
		self.assertEqual(expected, selection_sort(given))

	def test_selection_sort_5(self):
		given = []
		expected = []
		self.assertEqual(expected, selection_sort(given))

	def test_selection_sort_6(self):
		given = [1,3,5,7,9,10]
		expected = [1,3,5,7,9,10]
		self.assertEqual(expected, selection_sort(given))


if __name__ == "__main__":
	unittest.main()