import unittest

def zigzag_arrangement(arr):
	length = len(arr)
	if length <= 1:
		return arr

	for i in xrange(length-1):
		if i%2==0:
			if arr[i] > arr[i+1]:
				arr[i], arr[i+1] = arr[i+1], arr[i]
		elif arr[i] < arr[i+1]:
			arr[i], arr[i+1] = arr[i+1], arr[i]

	return arr


class TestZigzagArrangement(unittest.TestCase):

	def test_zigzag_arrangement_1(self):
		given = [4,3,7,8,6,2,1]
		result = [3,7,4,8,2,6,1]
		self.assertEqual(result, zigzag_arrangement(given))

	def test_zigzag_arrangement_2(self):
		given = [11,4,9,15,6,3,4,5]
		result = [4,11,9,15,3,6,4,5]
		self.assertEqual(result, zigzag_arrangement(given))

	def test_zigzag_arrangement_3(self):
		given = []
		result = []
		self.assertEqual(result, zigzag_arrangement(given))

	def test_zigzag_arrangement_4(self):
		given = [4]
		result = [4]
		self.assertEqual(result, zigzag_arrangement(given))

	def test_zigzag_arrangement_5(self):
		given = [-1,-2,-3]
		result = [-2,-1,-3]
		self.assertEqual(result, zigzag_arrangement(given))

if __name__ == "__main__":
	unittest.main()