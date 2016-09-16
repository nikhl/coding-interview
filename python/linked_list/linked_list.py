import unittest

class Node:

	def __init__(self, data=None, next=None):
		self._data = data
		self._next = next

	def set_next(self, node):
		self._next = node

	def get_next(self):
		return self._next

	def set_data(self, data):
		self._data = data

	def get_data(self):
		return self._data

class LinkedList:
	
	def __init__(self, head=None):
		self._head = head

	def get_head(self):
		return self._head

	def insert_at_head(self, node):
		# takes constant time, O(1)
		node.set_next(self._head)
		self._head = node

	def insert_at_tail(self, node):
		# takes linear time, O(n)
		if self._head is None:
			self._head = node
		else:
			curr = self._head
			# traverse linkedlist until we reach last element
			while curr.get_next():
				curr = curr.get_next()

			curr.set_next(node)

	def delete_at_head(self):
		# takes constant time, O(1)
		elem = None
		if self._head:
			elem = self.get_head()
			self._head = self._head.get_next()

		return elem

	def delete_at_tail(self):
		elem = None
		# takes constant time, O(n)
		if self._head:
			if self._head.get_next():
				curr = self._head
				# traverse linkedlist until we reach
				# last but one node
				while curr.get_next().get_next():
					curr = curr.get_next()

				elem = curr.get_next().get_data()
				curr.set_next(None)
			else:
				elem = self._head.get_data()
				self._head = None

		return elem

	def search(self, value):
		# search for a node with data=value and return the
		# index of that node. First node's index is 1 and so on.
		# if node is not found, return -1
		
		if not self._head:
			return -1

		if self._head.get_data() == value:
			return 1

		counter = 1
		current = self._head

		# traverse linkedlist until we find the node
		# or we reach end of linkedlist in which case
		# return -1
		while current:
			if current.get_data() == value:
				return counter

			counter += 1
			current = current.get_next()

		return -1


	def get_elements_list(self):
		# returns an array with element as node's data
		# from head to tail
		curr = self._head
		elements = []

		while curr:
			elements.append(curr.get_data())
			curr = curr.get_next()

		return elements



class TestLinkedList(unittest.TestCase):

	def setUp(self):
		self.ll = LinkedList()

	def test_insert_at_head(self):
		self.ll.insert_at_head(Node(1))
		self.assertEqual([1], self.ll.get_elements_list())
		self.ll.insert_at_head(Node(2))
		self.ll.insert_at_head(Node(3))
		self.ll.insert_at_head(Node(4))
		self.ll.insert_at_head(Node(5))
		self.ll.insert_at_head(Node(7))
		self.ll.insert_at_head(Node(6))
		self.assertEqual([6,7,5,4,3,2,1], self.ll.get_elements_list())

	def test_insert_at_tail(self):
		self.ll.insert_at_tail(Node(1))
		self.assertEqual([1], self.ll.get_elements_list())
		self.ll.insert_at_tail(Node(2))
		self.ll.insert_at_tail(Node(3))
		self.assertEqual([1,2,3], self.ll.get_elements_list())
		self.ll.insert_at_tail(Node(4))
		self.ll.insert_at_tail(Node(5))
		self.ll.insert_at_tail(Node(7))
		self.ll.insert_at_tail(Node(6))
		self.assertEqual([1,2,3,4,5,7,6], self.ll.get_elements_list())

	def test_delete_at_head(self):
		self.ll.insert_at_tail(Node(1))
		self.assertEqual([1], self.ll.get_elements_list())
		self.ll.insert_at_tail(Node(2))
		self.ll.insert_at_tail(Node(3))
		self.assertEqual([1,2,3], self.ll.get_elements_list())
		self.ll.insert_at_tail(Node(4))
		self.ll.insert_at_tail(Node(5))
		self.assertEqual([1,2,3,4,5], self.ll.get_elements_list())
		self.assertEqual(1, self.ll.delete_at_head())
		self.assertEqual(2, self.ll.delete_at_head())
		self.assertEqual([3,4,5], self.ll.get_elements_list())
		self.assertEqual(3, self.ll.delete_at_head())
		self.assertEqual([4,5], self.ll.get_elements_list())

	def test_delete_at_tail(self):
		self.ll.insert_at_tail(Node(1))
		self.assertEqual([1], self.ll.get_elements_list())
		self.ll.insert_at_tail(Node(2))
		self.ll.insert_at_tail(Node(3))
		self.assertEqual([1,2,3], self.ll.get_elements_list())
		self.ll.insert_at_tail(Node(4))
		self.ll.insert_at_tail(Node(5))
		self.assertEqual([1,2,3,4,5], self.ll.get_elements_list())
		self.assertEqual(5, self.ll.delete_at_tail())
		self.assertEqual(4, self.ll.delete_at_tail())
		self.assertEqual([1,2,3], self.ll.get_elements_list())
		self.assertEqual(3, self.ll.delete_at_tail())
		self.assertEqual([1,2], self.ll.get_elements_list())

	def test_search(self):
		self.ll.insert_at_tail(Node(1))
		self.assertEqual(1, self.ll.search(1))
		self.ll.insert_at_tail(Node(2))
		self.ll.insert_at_tail(Node(3))
		self.assertEqual(3, self.ll.search(3))
		self.ll.insert_at_tail(Node(4))
		self.ll.insert_at_tail(Node(5))
		self.assertEqual(4, self.ll.search(4))
		self.assertEqual(5, self.ll.delete_at_tail())
		self.assertEqual(4, self.ll.delete_at_tail())
		self.assertEqual(-1, self.ll.search(4))
		self.assertEqual(3, self.ll.delete_at_tail())
		self.assertEqual(2, self.ll.search(2))

if __name__ == "__main__":
	unittest.main()