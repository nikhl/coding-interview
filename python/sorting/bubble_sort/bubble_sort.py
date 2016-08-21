import unittest

def bubble_sort(nums):
	swaps = False
	length = len(nums)
	for i in range(length):
		for j in range(length-1):
			if nums[j] > nums[j+1]:
				swaps = True
				nums[j], nums[j+1] = nums[j+1], nums[j]

		if not swaps:
			return nums

	return nums

class TestBubbleSort(unittest.TestCase):

	def test_bubble_sort_1(self):
		given = [2,4,3,1,5]
		expected = [1,2,3,4,5]
		self.assertEqual(expected, bubble_sort(given))

	def test_bubble_sort_2(self):
		given = [5,4,3,2,1]
		expected = [1,2,3,4,5]
		self.assertEqual(expected, bubble_sort(given))

	def test_bubble_sort_3(self):
		given = [2,7,4,1,5,3]
		expected = [1,2,3,4,5,7]
		self.assertEqual(expected, bubble_sort(given))

	def test_bubble_sort_4(self):
		given = [2]
		expected = [2]
		self.assertEqual(expected, bubble_sort(given))

	def test_bubble_sort_5(self):
		given = []
		expected = []
		self.assertEqual(expected, bubble_sort(given))

	def test_bubble_sort_6(self):
		given = [1,3,5,7,9,10]
		expected = [1,3,5,7,9,10]
		self.assertEqual(expected, bubble_sort(given))


if __name__ == "__main__":
	unittest.main()