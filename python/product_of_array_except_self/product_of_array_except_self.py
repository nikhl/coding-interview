import unittest

def product_except_self(arr):
	length = len(arr)
	if length<=1:
		return arr

	# Initialize fwd and rev prods and result
	fwd_prod = [1]*length
	rev_prod = [1]*length
	result = [1]*length

	# calcute products in forward direction except self
	# notice fwd_prod[0] is always 1
	for i in xrange(1,length):
		fwd_prod[i] = fwd_prod[i-1]*arr[i-1]

	# calcute products in reverse direction except self
	# notice rev_prod[-1] is always 1
	for i in xrange(length-2,-1,-1):
		rev_prod[i] = rev_prod[i+1]*arr[i+1]

	# product_except_self[i] is product of
	# fwd_prod[i] and rev_prod[i]
	for i in xrange(length):
		result[i] = fwd_prod[i]*rev_prod[i]

	return result

class TestProductExceptSelf(unittest.TestCase):

	def test_product_array_except_self_1(self):
		given = [1,2,3,4]
		result = [24,12,8,6]
		self.assertEqual(result, product_except_self(given))

	def test_product_array_except_self_2(self):
		given = [1]
		result = [1]
		self.assertEqual(result, product_except_self(given))

	def test_product_array_except_self_3(self):
		given = []
		result = []
		self.assertEqual(result, product_except_self(given))

	def test_product_array_except_self_4(self):
		given = [10,20]
		result = [20,10]
		self.assertEqual(result, product_except_self(given))

	def test_product_array_except_self_5(self):
		given = [10,20,0,20,10]
		result = [0,0,40000,0,0]
		self.assertEqual(result, product_except_self(given))

if __name__ == "__main__":
	unittest.main()