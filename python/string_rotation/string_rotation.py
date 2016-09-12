import unittest


def is_string_rotated(str1, str2):
	# check if str2 is rotation of str1
	if str1==str2:
		return True

	for i in xrange(len(str2)):
		if str1 == str2[i:]+str2[:i]:
			return True

	return False

class TestStringRotation(unittest.TestCase):

	def test_string_rotation_1(self):
		self.assertTrue(is_string_rotated("abc","abc"))

	def test_string_rotation_2(self):
		self.assertTrue(is_string_rotated("abc","cab"))

	def test_string_rotation_3(self):
		self.assertTrue(is_string_rotated("",""))

	def test_string_rotation_4(self):
		self.assertFalse(is_string_rotated("abc",""))

	def test_string_rotation_5(self):
		self.assertTrue(is_string_rotated("abcdef","defabc"))

if __name__ == "__main__":
	unittest.main()