import unittest

class MaxHeap:

	def __init__(self):
		# we always skip 0th element in array
		# for convenience so
		# kth elements left child is 2*k
		# kth elements right child is (2*k)+1
		# kth elements parent is k/2
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

			# if left child is greater than right child
			if self._arr[left_index] > self._arr[right_index]:
				
				# if left child is also bigger than parent,
				# swap parent and left child and call
				# percolate_up recursilvely on current index's parent
				# if left child is smaller than parent that means
				# parent is already greater than children, so
				# no more work to do
				if self._arr[left_index] > self._arr[index]:
					self._arr[index], self._arr[left_index] = \
						self._arr[left_index], self._arr[index]
					self.percolate_up(index/2)

			# if right child is greater than parent, swap parent
			# and right child and call percolate_up recursively
			# on current index's parent
			# if right child is smaller than parent that means
			# parent is already greater than children, so
			# no more work to do
			elif self._arr[right_index] > self._arr[index]:
				self._arr[index], self._arr[right_index] = \
					self._arr[right_index], self._arr[index]
				self.percolate_up(index/2)

		# if only left child needs to be considered
		elif (left_index) <= length:
			if self._arr[left_index] > self._arr[index]:
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

	def find_max(self):
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

			# if left child is greater than right child
			if self._arr[left_index] > self._arr[right_index]:

				# if left child is also bigger than parent,
				# swap parent and left child and call
				# percolate_down recursilvely on left child
				# if left child is smaller than parent that means
				# parent is already greater than children, so
				# no more work to do
				if self._arr[left_index] > self._arr[index]:
					self._arr[left_index], self._arr[index] = \
						self._arr[index], self._arr[left_index]
					self.percolate_down(left_index)

			# if right child is greater than parent, swap parent
			# and right child and call percolate_down recursively
			# on right child
			# if right child is smaller than parent that means
			# parent is already greater than children, so
			# no more work to do
			elif self._arr[right_index] > self._arr[index]:
				self._arr[index], self._arr[right_index] = \
					self._arr[right_index], self._arr[index]
				self.percolate_down(right_index)

		# if only left child needs to be considered
		elif left_index <= length:
			if self._arr[left_index] > self._arr[index]:
				self._arr[left_index], self._arr[index] = \
					self._arr[index], self._arr[left_index]
				self.percolate_down(left_index)
		
		# if current index has no children, no comparisons
		# needs to be done and the priority queue is fixed
		else:
			return


	def extract_max(self):
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


class TestMaxHeap(unittest.TestCase):

	def setUp(self):
		self.maxheap = MaxHeap()

	def test_insert(self):
		self.maxheap.insert(10)
		self.assertEqual(10, self.maxheap.find_max())
		self.maxheap.insert(11)
		self.assertEqual(11, self.maxheap.find_max())
		self.maxheap.insert(9)
		self.assertEqual(11, self.maxheap.find_max())
		self.maxheap.insert(13)
		self.assertEqual(13, self.maxheap.find_max())

	def test_find_max(self):
		self.assertRaises(Exception, self.maxheap.find_max)
		self.maxheap.insert(0)
		self.assertEqual(0, self.maxheap.find_max())
		self.maxheap.insert(-1)
		self.assertEqual(0, self.maxheap.find_max())
		self.maxheap.insert(9)
		self.assertEqual(9, self.maxheap.find_max())
		self.maxheap.insert(9)
		self.assertEqual(9, self.maxheap.find_max())

	def test_extract_max(self):
		self.assertRaises(Exception, self.maxheap.extract_max)
		self.maxheap.insert(0)
		self.assertEqual(0, self.maxheap.extract_max())
		self.maxheap.insert(-1)
		self.assertEqual(-1, self.maxheap.extract_max())
		self.assertRaises(Exception, self.maxheap.extract_max)
		self.maxheap.insert(9)
		self.maxheap.insert(8)
		self.assertEqual(9, self.maxheap.extract_max())
		self.assertEqual(8, self.maxheap.extract_max())
		self.maxheap.insert(17)
		self.assertEqual(17, self.maxheap.extract_max())
		self.assertRaises(Exception, self.maxheap.extract_max)

if __name__ == "__main__":
	unittest.main()
