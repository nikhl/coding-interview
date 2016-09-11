# Suppose a sorted array is rotated at some pivot
# unknown to you beforehand.
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
# You are given a target value to search. If found in the array
# return its index, otherwise return -1.
# You may assume no duplicate exists in the array.

import unittest

def rotated_binary_search(arr, key):
	if not arr:
		return False

	if len(arr)==1:
		return arr[0]==key

	left = 0
	right = len(arr)-1

	while left <= right:
		mid = (left+right)/2
		if arr[mid]==key:
			return mid

		if arr[mid] < arr[left]:
			# mid to end array is sorted
			if arr[mid] < key and arr[right] >= key:
				left = mid + 1
			else:
				right = mid - 1

		# left..mid array is sorted
		if arr[mid] > key and arr[left] <= key:
			right = mid - 1
		else:
			left = mid + 1

	return False


class TestRotatedBinarySearch(unittest.TestCase):

	def test_rotated_binary_search_1(self):
		self.assertEqual(6, rotated_binary_search([4,5,6,7,0,1,2], 2))

	def test_rotated_binary_search_2(self):
		self.assertEqual(4, rotated_binary_search([0,1,2,3,4,5,6,7], 4))

	def test_rotated_binary_search_3(self):
		self.assertEqual(0, rotated_binary_search([70,10,20,30,40,50], 70))

	def test_rotated_binary_search_4(self):
		self.assertFalse(rotated_binary_search([1], 2))

	def test_rotated_binary_search_5(self):
		self.assertEqual(5, rotated_binary_search([5,6,7,8,9,10,0], 10))

if __name__ == "__main__":
	unittest.main()