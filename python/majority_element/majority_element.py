import unittest


def get_majority_element(arr):
	if not arr:
		return None

	if len(arr)==1:
		return arr[0]

	# start assuming first element as majority element
	maj_elem = arr[0]
	memo = {maj_elem:1}

	for i in xrange(1,len(arr)):
		if maj_elem != arr[i]:
			# decrease count of current majority element
			memo[maj_elem] -= 1

			# if count becomes zero, delete previous maj_element
			# and make current element as maj_element with count 1
			if memo[maj_elem] == 0:
				del memo[maj_elem]
				maj_elem = arr[i]
				memo[maj_elem] = 1

		# increase the count if current element is same as maj_element
		else:
			memo[maj_elem] += 1


	return maj_elem


class TestMajorityElement(unittest.TestCase):

	def test_majority_element_1(self):
		self.assertEqual(4,get_majority_element([1,2,3,4,4,4,4,5,4]))

	def test_majority_element_2(self):
		self.assertEqual(4,get_majority_element([4]))

	def test_majority_element_3(self):
		self.assertEqual(4,get_majority_element([1,4,1,4,1,4,4]))

	def test_majority_element_4(self):
		self.assertEqual(3,get_majority_element([1,2,3,2,3,3]))

	def test_majority_element_5(self):
		self.assertEqual(0,get_majority_element([0,0,0]))

if __name__ == "__main__":
	unittest.main()