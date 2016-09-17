import unittest

class MinHeap:

	def __init__(self):
		# we always skip 0th element in array
		# for convenience so that
		# kth element's left child is 2*k
		# kth element's right child is (2*k)+1
		# kth element's parent is k/2
		self._arr = [0]

	def percolate_up(self, index):
		if index < 1:
			return

		length = len(self._arr)
		left_index = 2*index
		right_index = (2*index)+1

		# if for current index, both left child and right child
		# needs to be considered
		if (left_index < length) and (right_index < length):

			# if left child is smaller than right child
			if self._arr[left_index] < self._arr[right_index]:
				
				# if left child is also smaller than parent,
				# swap parent and left child and call
				# percolate_up recursilvely on current index's parent
				# if left child is greater than parent that means
				# parent is already smaller than children, so
				# no more work to do
				if self._arr[left_index] < self._arr[index]:
					self._arr[index], self._arr[left_index] = \
						self._arr[left_index], self._arr[index]
					self.percolate_up(index/2)

			# if right child is smaller than parent, swap parent
			# and right child and call percolate_up recursively
			# on current index's parent
			# if right child is greater than parent that means
			# parent is already smaller than children, so
			# no more work to do
			elif self._arr[right_index] < self._arr[index]:
				self._arr[index], self._arr[right_index] = \
					self._arr[right_index], self._arr[index]
				self.percolate_up(index/2)

		# if only left child needs to be considered
		elif (left_index) <= length:
			if self._arr[left_index] < self._arr[index]:
				self._arr[index], self._arr[left_index] = \
					self._arr[left_index], self._arr[index]
				self.percolate_up(index/2)

		# if current index has no children, no comparisons
		# to be done and call percolate_up recursively on
		# current index's parent
		else:
			self.percolate_up(index/2)


	def insert(self, data):
		self._arr.append(data)
		if not len(self._arr) == 2:
			self.percolate_up(len(self._arr)-1)

	def find_min(self):
		if len(self._arr) <= 1:
			raise Exception("Priority Queue is empty")

		return self._arr[1]


	def percolate_down(self, index):
		length = len(self._arr)-1
		if index > length:
			return

		left_index = 2*index
		right_index = (2*index)+1

		# if for current index, both left child and right child
		# needs to be considered
		if (left_index <= length) and (right_index <= length):

			# if left child is smaller than right child
			if self._arr[left_index] < self._arr[right_index]:

				# if left child is also smaller than parent,
				# swap parent and left child and call
				# percolate_down recursilvely on left child
				# if left child is greater than parent that means
				# parent is already smaller than children, so
				# no more work to do
				if self._arr[left_index] < self._arr[index]:
					self._arr[left_index], self._arr[index] = \
						self._arr[index], self._arr[left_index]
					self.percolate_down(left_index)

			# if right child is smaller than parent, swap parent
			# and right child and call percolate_down recursively
			# on right child
			# if right child is greater than parent that means
			# parent is already smaller than children, so
			# no more work to do
			elif self._arr[right_index] < self._arr[index]:
				self._arr[index], self._arr[right_index] = \
					self._arr[right_index], self._arr[index]
				self.percolate_down(right_index)

		# if only left child needs to be considered
		elif left_index <= length:
			if self._arr[left_index] < self._arr[index]:
				self._arr[left_index], self._arr[index] = \
					self._arr[index], self._arr[left_index]
				self.percolate_down(left_index)
		
		# if current index has no children, no comparisons
		# needs to be done and the priority queue is fixed
		else:
			return


	def extract_min(self):
		if len(self._arr) <= 1:
			raise Exception("Priority Queue is empty")

		if len(self._arr) == 2:
			elem = self._arr.pop()
			return elem

		elem = self._arr[1]
		self._arr[1] = self._arr[-1]
		self._arr.pop()

		if len(self._arr) > 2:
			self.percolate_down(1)

		return elem

	def get_array_representation(self):
		return self._arr


class TestMinHeap(unittest.TestCase):

	def setUp(self):
		self.minheap = MinHeap()

	def test_insert(self):
		self.minheap.insert(10)
		self.assertEqual(10, self.minheap.find_min())
		self.minheap.insert(11)
		self.assertEqual(10, self.minheap.find_min())
		self.minheap.insert(9)
		self.assertEqual(9, self.minheap.find_min())
		self.minheap.insert(13)
		self.assertEqual(9, self.minheap.find_min())
		self.minheap.insert(3)
		self.assertEqual(3, self.minheap.find_min())

	def test_find_min(self):
		self.assertRaises(Exception, self.minheap.find_min)
		self.minheap.insert(0)
		self.assertEqual(0, self.minheap.find_min())
		self.minheap.insert(-1)
		self.assertEqual(-1, self.minheap.find_min())
		self.minheap.insert(9)
		self.assertEqual(-1, self.minheap.find_min())
		self.minheap.insert(-10)
		self.assertEqual(-10, self.minheap.find_min())

	def test_extract_min(self):
		self.assertRaises(Exception, self.minheap.extract_min)
		self.minheap.insert(0)
		self.assertEqual(0, self.minheap.extract_min())
		self.minheap.insert(-1)
		self.assertEqual(-1, self.minheap.extract_min())
		self.assertRaises(Exception, self.minheap.extract_min)
		self.minheap.insert(9)
		self.minheap.insert(8)
		self.assertEqual(8, self.minheap.extract_min())
		self.assertEqual(9, self.minheap.extract_min())
		self.minheap.insert(17)
		self.assertEqual(17, self.minheap.extract_min())
		self.assertRaises(Exception, self.minheap.extract_min)

if __name__ == "__main__":
	unittest.main()
