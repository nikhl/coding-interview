# Reverse digits of an integer.
# Example1: x = 123, return 321
# Example2: x = -123, return -321

import unittest
import math

def reverse_integer(number):
	num = abs(number)
	if num<10:
		return number

	nums = []
	# extract each digit and append it to nums array
	while num>9:
		nums.append(num%10)
		num = num/10

	nums.append(num)

	solution = 0
	for i in xrange(len(nums)):
		solution += nums[i] * int(math.pow(10, (len(nums)-i-1)))

	if number < 0:
		return -solution

	return solution


class TestReverseInteger(unittest.TestCase):

	def test_reverse_integer_1(self):
		self.assertEqual(321, reverse_integer(123))

	def test_reverse_integer_2(self):
		self.assertEqual(-321, reverse_integer(-123))

	def test_reverse_integer_3(self):
		self.assertEqual(1, reverse_integer(1))

	def test_reverse_integer_4(self):
		self.assertEqual(-9, reverse_integer(-90000))

	def test_reverse_integer_5(self):
		self.assertEqual(91239, reverse_integer(93219))

if __name__ == "__main__":
	unittest.main()