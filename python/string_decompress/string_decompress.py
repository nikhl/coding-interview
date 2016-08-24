import unittest
import math


def string_decompress(compressed_str):
	if not compressed_str:
		return ""

	compressed = compressed_str
	result = ""

	while compressed:
		nums = []
		count = 0

		# collect all int's until we reach a charecter
		# we assume char to be within ASCII range 65-90
		# everything else is an integer
		while ord(compressed[0]) not in range(65, 65+26):
			nums.append(int(compressed[0]))
			compressed = compressed[1:]

		# read the charecter and remove it from compressed
		char = compressed[0]
		compressed = compressed[1:]
		
		# from extracted nums, calculate actual count
		nums_length = len(nums)
		for i in range(nums_length):
			count += int(nums[i] * (math.pow(10, nums_length-i-1)))

		# assume count=1 if there is no number preceding a char
		if count==0:
			count = 1

		while count > 0:
			result += char
			count -= 1

	return result



class TestStringDecompress(unittest.TestCase):

	def test_decompress_1(self):
		compressed = "4A2BC2A"
		decompressed = "AAAABBCAA"
		self.assertEqual(decompressed, string_decompress(compressed))

	def test_decompress_2(self):
		compressed = ""
		decompressed = ""
		self.assertEqual(decompressed, string_decompress(compressed))

	def test_decompress_3(self):
		compressed = "ABC"
		decompressed = "ABC"
		self.assertEqual(decompressed, string_decompress(compressed))

	def test_decompress_4(self):
		compressed = "A3B5C6F"
		decompressed = "ABBBCCCCCFFFFFF"
		self.assertEqual(decompressed, string_decompress(compressed))

	def test_decompress_5(self):
		compressed = "AB3C"
		decompressed = "ABCCC"
		self.assertEqual(decompressed, string_decompress(compressed))

	def test_decompress_6(self):
		compressed = "ABCABC"
		decompressed = "ABCABC"
		self.assertEqual(decompressed, string_decompress(compressed))

	def test_decompress_7(self):
		compressed = "A"
		decompressed = "A"
		self.assertEqual(decompressed, string_decompress(compressed))

	def test_decompress_8(self):
		compressed = "10A"
		decompressed = "AAAAAAAAAA"
		self.assertEqual(decompressed, string_decompress(compressed))

	def test_decompress_9(self):
		compressed = "10AB11C"
		decompressed = "AAAAAAAAAABCCCCCCCCCCC"
		self.assertEqual(decompressed, string_decompress(compressed))

if __name__ == "__main__":
	unittest.main()