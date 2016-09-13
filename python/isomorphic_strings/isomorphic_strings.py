import unittest

def is_isomorphic(str1, str2):
	# if two strings are different lengths, return False
	if len(str1) != len(str2):
		return False

	memo = {}
	visited = set()

	for i in xrange(len(str1)):
		if str1[i] in memo:
			# if str1[i] is already in memo, we already have an associated
			# char for str1[i] stored in memo. check if str2[i] is same as
			# memo[str1[i]]. If not, return False
			if str2[i] != memo[str1[i]]:
				return False
		else:
			# if we are seeing str1[i] for first time but str2[i] is
			# already seen, return False because every occurance of str1[i]
			# should have memo[str1[i]] as str2[i]
			if str2[i] in visited:
				return False

			# add the mapping to memo and add str2[i] to visited
			memo[str1[i]] = str2[i]
			visited.add(str2[i])

	return True


class TestIsomorphicStrings(unittest.TestCase):

	def test_isomorphic_strings_1(self):
		self.assertTrue(is_isomorphic("add", "egg"))

	def test_isomorphic_strings_2(self):
		self.assertFalse(is_isomorphic("foo", "bar"))

	def test_isomorphic_strings_3(self):
		self.assertTrue(is_isomorphic("paper", "title"))

	def test_isomorphic_strings_4(self):
		self.assertTrue(is_isomorphic("a", "b"))

	def test_isomorphic_strings_5(self):
		self.assertFalse(is_isomorphic("", "egg"))

	def test_isomorphic_strings_6(self):
		self.assertTrue(is_isomorphic("", ""))

	def test_isomorphic_strings_7(self):
		self.assertFalse(is_isomorphic("abb", "ccc"))

	def test_isomorphic_strings_8(self):
		self.assertFalse(is_isomorphic("aab", "xyz"))

if __name__ == "__main__":
	unittest.main()