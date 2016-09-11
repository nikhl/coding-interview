# Determine whether an integer is a palindrome.
# Do this without extra space.

import unittest

def is_palindrome_number(num):

	if num<0:
		# if num is negative, return False
		return False

	if num < 10:
		# single digit nums are always palindromes
		return True

	rev_number = 0
	x = num
	
	# determine the length of given num
	# length will be used to calculate rev_number
	length = 0
	while x>0:
		x = x/10
		length += 1

	x = num
	for i in xrange(length):
		digit = x % 10
		x = x / 10
		rev_number = rev_number + digit * (10**(length-i-1))

	return rev_number == num


class TestPalindromeNumber(unittest.TestCase):

	def test_palindrome_number_1(self):
		self.assertTrue(is_palindrome_number(123321))

	def test_palindrome_number_2(self):
		self.assertTrue(is_palindrome_number(11))

	def test_palindrome_number_3(self):
		self.assertFalse(is_palindrome_number(123421))

	def test_palindrome_number_4(self):
		self.assertTrue(is_palindrome_number(1))

	def test_palindrome_number_5(self):
		self.assertFalse(is_palindrome_number(1233210))

if __name__ == "__main__":
	unittest.main()