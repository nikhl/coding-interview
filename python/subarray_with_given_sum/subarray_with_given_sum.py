import unittest

def sub_array_with_sum(arr, total):
	# if arr is empty, return (-1,-1)
	if not arr:
		return (-1,-1)

	# if first element in array is equal to total
	# return (1,1)
	if arr[0] == total:
		return (1,1)

	# initialize start, end, length and curr_sum
	start = 0
	end = 0
	length = len(arr)
	curr_sum = arr[0]

	while start <= end:
		# add arr[end] to curr_sum as long as
		# curr_sum does not exceed total
		while (end <= length-1) and (curr_sum < total):
			# increment end and add arr[end]
			# to curr_sum
			end += 1
			curr_sum += arr[end]

			# if curr_sum eqauls total,
			# stop and return (start+1,end+1)
			# since array indices start with 0
			if curr_sum == total:
				return (start+1, end+1)		

		# if end reaches out of array, return (-1,-1)
		if end >= length:
			return (-1,-1)

		# at this point, curr_sum exceeded total
		# remove arr[end] from curr_sum and decreement end
		curr_sum -= arr[end]
		end -= 1

		# remove arr[start] from curr_sum and increment start
		curr_sum -= arr[start]
		start += 1

	return (-1,-1)


class TestSubArraySum(unittest.TestCase):

	def test_sub_array_sum_1(self):
		given = [1,2,3,7,5]
		total = 12
		self.assertEqual((2,4), sub_array_with_sum(given, total))

	def test_sub_array_sum_2(self):
		given = [1,2,3,4,5,6,7,8,9,10]
		total = 15
		self.assertEqual((1,5), sub_array_with_sum(given, total))

	def test_sub_array_sum_3(self):
		given = [1,2,3,7,5]
		total = 1
		self.assertEqual((1,1), sub_array_with_sum(given, total))

	def test_sub_array_sum_4(self):
		given = []
		total = 1
		self.assertEqual((-1,-1), sub_array_with_sum(given, total))

if __name__ == "__main__":
	unittest.main()