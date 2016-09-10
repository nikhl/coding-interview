# Given an array of integers, return indices of the two numbers
# such that they add up to a specific target.

# Return all pairs if there are multiple solutions

import unittest

def two_sum_ver2(arr, key):
	# this works when there are multiple solutions
	# and it returns all pairs
	memo = {}
	solutions = []

	for i in xrange(len(arr)):
		if (key-arr[i]) in memo:
			# found a pair and add it to solution
			solutions.append((memo[key-arr[i]].pop(), i))

			# after using an index for solution, check if
			# there are more indices associated with (key-arr[i])
			# if not, delete (key-arr[i]) from memo
			if not memo[key-arr[i]]:
				del memo[key-arr[i]]

		# if arr[i] is already in memo, append current index
		elif arr[i] in memo:
			memo[arr[i]].append(i)
		# if arr[i] is not in memo, initialize and add
		else:
			memo[arr[i]] = []
			memo[arr[i]].append(i)

	return solutions

class TestTwoSum(unittest.TestCase):

	def test_two_sum_1(self):
		self.assertEqual([(0,1)], two_sum_ver2([2,7,7,9], 9))

	def test_two_sum_2(self):
		self.assertEqual([(0,1), (2,3)], two_sum_ver2([1,2,2,1], 3))

	def test_two_sum_3(self):
		self.assertEqual([(1, 3)], two_sum_ver2([2,7,11,15], 22))

	def test_two_sum_4(self):
		self.assertEqual([(0,2),(1,3)], two_sum_ver2([15, 12, 10, 13], 25))

	def test_two_sum_5(self):
		self.assertEqual([(4,5),(0,7)], two_sum_ver2([520, 20, 33, 41, 567, 3, 90, 50], 570))

if __name__ == "__main__":
	unittest.main()