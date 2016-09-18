import unittest

# use linked_list and Node from
# https://github.com/nikhl/coding_interview/tree/master/python/linked_list
from linked_list import LinkedList
from linked_list import Node

class ListInsertionSort(LinkedList):

	def compare_and_insert(self, node):
		# if list is empty, make node the head
		# of linked list and return
		if not self._head:
			self._head = node
			return

		# if node's data is smaller than head's data
		# make node as head of list and return
		if node.get_data() <= self._head.get_data():
			node.set_next(self._head)
			self._head = node
			return

		curr = self._head

		# traverse the list until we find a node whose
		# next node's data is greater than node's data
		while curr.get_next() and curr.get_next().get_data() <= node.get_data():
			curr = curr.get_next()

		# insert node after curr and return
		node.set_next(curr.get_next())
		curr.set_next(node)


def insertion_sort(arr):
	# if arr is empty of just has one element
	# it is already sorted, so return arr
	if len(arr) <= 1:
		return arr

	insertion_list = ListInsertionSort()

	# insert each element into insertion_list
	for i in arr:
		insertion_list.compare_and_insert(Node(i))

	return insertion_list.get_elements_list()

class TestInsertionSort(unittest.TestCase):

	def test_insertion_sort_1(self):
		given = [2,4,3,1,5]
		expected = [1,2,3,4,5]
		self.assertEqual(expected, insertion_sort(given))

	def test_insertion_sort_2(self):
		given = [5,4,3,2,1]
		expected = [1,2,3,4,5]
		self.assertEqual(expected, insertion_sort(given))

	def test_insertion_sort_3(self):
		given = [2,7,4,1,5,3]
		expected = [1,2,3,4,5,7]
		self.assertEqual(expected, insertion_sort(given))

	def test_insertion_sort_4(self):
		given = [2]
		expected = [2]
		self.assertEqual(expected, insertion_sort(given))

	def test_insertion_sort_5(self):
		given = []
		expected = []
		self.assertEqual(expected, insertion_sort(given))

	def test_insertion_sort_6(self):
		given = [1,3,5,7,9,10]
		expected = [1,3,5,7,9,10]
		self.assertEqual(expected, insertion_sort(given))


if __name__ == "__main__":
	unittest.main()