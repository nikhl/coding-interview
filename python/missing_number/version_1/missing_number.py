import unittest

def missing_number(arr):
	# assume numbers always start from 0 or 1
	sum = 0
	n = len(arr)

	for i in arr:
		sum += i

	return (((n)*(n+1))/2) - sum

class TestMissingNumber(unittest.TestCase):

	def test_missing_number_1(self):
		given = [0,1,3]
		missing = 2
		self.assertEqual(missing, missing_number(given))

	def test_missing_number_2(self):
		given = [0,1,2,3,4,5,6,7,9]
		missing = 8
		self.assertEqual(missing, missing_number(given))

if __name__ == "__main__":
	unittest.main()