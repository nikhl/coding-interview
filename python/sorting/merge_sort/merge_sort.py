import unittest

def merge_sort(arr):

	length = len(arr)

	if length <= 1:
		return arr

	left = arr[:length/2]
	right = arr[length/2:]

	return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
	result = []

	while left and right:
		if left[0] > right[0]:
			result.append(right[0])
			right = right[1:]
		else:
			result.append(left[0])
			left = left[1:]

	if not left:
		result.extend(right)

	if not right:
		result.extend(left)

	return result



class TestMergeSort(unittest.TestCase):

	def test_merge_sort_1(self):
		given = [2,4,3,1,5]
		expected = [1,2,3,4,5]
		self.assertEqual(expected, merge_sort(given))

	def test_merge_sort_2(self):
		given = [5,4,3,2,1]
		expected = [1,2,3,4,5]
		self.assertEqual(expected, merge_sort(given))

	def test_merge_sort_3(self):
		given = [2,7,4,1,5,3]
		expected = [1,2,3,4,5,7]
		self.assertEqual(expected, merge_sort(given))

	def test_merge_sort_4(self):
		given = [2]
		expected = [2]
		self.assertEqual(expected, merge_sort(given))

	def test_merge_sort_5(self):
		given = []
		expected = []
		self.assertEqual(expected, merge_sort(given))

	def test_merge_sort_6(self):
		given = [1,3,5,7,9,10]
		expected = [1,3,5,7,9,10]
		self.assertEqual(expected, merge_sort(given))


if __name__ == "__main__":
	unittest.main()