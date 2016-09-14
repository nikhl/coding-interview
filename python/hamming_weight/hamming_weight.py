import unittest

def hamming_weight(num):
	count = 0

	while num > 0:
		# bitwise and a number with 1 counts if rightmost bit
		# is set or not. Doing this by right shifting num each time
		# gives set bit count
		count += (num&1)
		num >>= 1

	return count


def brian_kernighan_count(num):
	count = 0

	while num > 0:
		# num & (num-1) toggles the rightmost set bit
		# count of how many such toggles returns set bit count
		num = num & (num-1)
		count += 1

	return count

class TestHammingWeight(unittest.TestCase):

	def test_hamming_weight_1(self):
		self.assertEqual(2, hamming_weight(6))

	def test_hamming_weight_2(self):
		self.assertEqual(3, hamming_weight(13))

	def test_hamming_weight_3(self):
		self.assertEqual(0, hamming_weight(0))

	def test_hamming_weight_4(self):
		self.assertEqual(1, hamming_weight(1))

	def test_brian_kernighan_1(self):
		self.assertEqual(2, brian_kernighan_count(6))

	def test_brian_kernighan_2(self):
		self.assertEqual(3, brian_kernighan_count(13))

	def test_brian_kernighan_3(self):
		self.assertEqual(0, brian_kernighan_count(0))

	def test_brian_kernighan_4(self):
		self.assertEqual(1, brian_kernighan_count(1))

if __name__ == "__main__":
	unittest.main()