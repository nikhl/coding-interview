import unittest

def missing_number(arr):
	if len(arr) <= 1:
		return None

	min_num = arr[1]

	# find minimum element from array
	for num in arr:
		if num < min_num:
			min_num = num

	# create an array num_check of length, len(arr)+1
	# with each element initialized to 0
	length = len(arr)
	num_check = [0] * (length+1)

	# since the numbers in arr are consecutive, mark all
	# (num-min_num) to 1's. After this, there will be only
	# one 0 in entire num_check array
	for num in arr:
		num_check[num-min_num] = 1

	# find index of number 0, min_num+i gives the missing number
	for i in xrange(len(num_check)):
		if num_check[i] == 0:
			return min_num + i



class TestMissingNumber(unittest.TestCase):

	def test_missing_number_1(self):
		given = [5,6,8]
		missing = 7
		self.assertEqual(missing, missing_number(given))

	def test_missing_number_2(self):
		given = [0,1,2,3,4,5,6,7,9]
		missing = 8
		self.assertEqual(missing, missing_number(given))

	def test_missing_number_3(self):
		given = [0,2,3,4,5,6,7,8,9]
		missing = 1
		self.assertEqual(missing, missing_number(given))

	def test_missing_number_4(self):
		given = [1,4,5,2,8,6,7]
		missing = 3
		self.assertEqual(missing, missing_number(given))

	def test_missing_number_5(self):
		given = [1,4,3]
		missing = 2
		self.assertEqual(missing, missing_number(given))

if __name__ == "__main__":
	unittest.main()