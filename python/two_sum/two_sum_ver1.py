# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.

# You may assume that each input would have exactly one solution.

import unittest

def two_sum_ver1(arr, key):
	# this assumes there is exactly one solution
	memo = {}

	for i in xrange(len(arr)):
		if (key-arr[i]) in memo:
			return [memo[key-arr[i]], i]
		else:
			memo[arr[i]] = i


class TestTwoSum(unittest.TestCase):

	def test_two_sum_1(self):
		self.assertEqual([0, 1], two_sum_ver1([2,7,11,15], 9))

	def test_two_sum_2(self):
		self.assertEqual([0, 1], two_sum_ver1([1,2], 3))

	def test_two_sum_3(self):
		self.assertEqual([1, 3], two_sum_ver1([2,7,11,15], 22))

	def test_two_sum_4(self):
		self.assertEqual([2, 3], two_sum_ver1([15, 12, 11, 13], 24))

	def test_two_sum_5(self):
		self.assertEqual([4, 5], two_sum_ver1([29, 20, 33, 41, 567, 3, 90, 26], 570))

if __name__ == "__main__":
	unittest.main()