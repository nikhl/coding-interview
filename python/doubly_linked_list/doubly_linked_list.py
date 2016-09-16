import unittest

class Node:

	def __init__(self, data=None, prev=None, next=None):
		self._data = data
		self._prev = prev
		self._next = next

	def get_prev(self):
		return self._prev

	def set_prev(self, node):
		self._prev = node

	def get_next(self):
		return self._next

	def set_next(self, node):
		self._next = node

	def get_data(self):
		return self._data

	def set_data(self, value):
		self._data = value

class DoublyLinkedList:

	def __init__(self):
		self._head = None
		self._tail = None

	def insert_at_head(self, node):
		# if doubly linked list is empty
		# make head and tail point to node
		if not self._head:
			self._head = node
			self._tail = node
		# set current head's prev to node and
		# set node's next to current head
		# make node as head of doubly linked list
		else:
			node.set_next(self._head)
			self._head.set_prev(node)
			self._head = node

	def insert_at_tail(self, node):
		# if doubly linked list is empty
		# make head and tail point to node
		if not self._tail:
			self._head = node
			self._tail = node
		# set current tail's next to node and
		# set node's prev to current tail
		# make node as tail of doubly linked list
		else:
			self._tail.set_next(node)
			node.set_prev(self._tail)
			self._tail = node

	def delete_at_head(self):
		node = None

		if self._head:
			node = self._head
			next_node = self._head.get_next()
			if next_node:
				next_node.set_prev(None)
				self._head = next_node
			else:
				self._head = None
				self._tail = None

		return node

	def delete_at_tail(self):
		node = None

		if self._tail:
			node = self._tail
			prev_node = self._tail.get_prev()
			if prev_node:
				prev_node.set_next(None)
				self._tail = prev_node
			else:
				self._head = None
				self._tail = None

		return node

	def search(self, key):
		# search for a node with data=key and return the
		# index of that node. First node's index is 1 and so on.
		# if key is not found, return -1
		if not self._head:
			return -1

		index = 1
		curr = self._head
		while curr:
			if curr.get_data() == key:
				return index

			index += 1
			curr = curr.get_next()

		return -1

	def get_elements_list(self):
		elements = []

		if not self._head:
			return elements

		curr = self._head

		while curr:
			elements.append(curr.get_data())
			curr = curr.get_next()

		return elements


class TestDoublyLinkedList(unittest.TestCase):

	def setUp(self):
		self.dll = DoublyLinkedList()

	def test_insert_at_head(self):
		self.dll.insert_at_head(Node(1))
		self.assertEqual([1], self.dll.get_elements_list())
		self.dll.insert_at_head(Node(2))
		self.dll.insert_at_head(Node(3))
		self.dll.insert_at_head(Node(4))
		self.assertEqual([4,3,2,1], self.dll.get_elements_list())
		self.dll.insert_at_head(Node(5))
		self.dll.insert_at_head(Node(6))
		self.assertEqual([6,5,4,3,2,1], self.dll.get_elements_list())

	def test_insert_at_tail(self):
		self.dll.insert_at_tail(Node(1))
		self.assertEqual([1], self.dll.get_elements_list())
		self.dll.insert_at_tail(Node(2))
		self.dll.insert_at_tail(Node(3))
		self.dll.insert_at_tail(Node(4))
		self.assertEqual([1,2,3,4], self.dll.get_elements_list())
		self.dll.insert_at_tail(Node(5))
		self.dll.insert_at_tail(Node(6))
		self.assertEqual([1,2,3,4,5,6], self.dll.get_elements_list())

	def test_delete_at_head(self):
		self.dll.insert_at_tail(Node(1))
		self.assertEqual(1, self.dll.delete_at_head().get_data())
		self.assertEqual([], self.dll.get_elements_list())
		self.dll.insert_at_head(Node(5))
		self.dll.insert_at_tail(Node(1))
		self.dll.insert_at_head(Node(4))
		self.dll.insert_at_tail(Node(3))
		self.assertEqual(4, self.dll.delete_at_head().get_data())
		self.assertEqual(5, self.dll.delete_at_head().get_data())
		self.assertEqual(1, self.dll.delete_at_head().get_data())
		self.assertEqual([3], self.dll.get_elements_list())
		self.assertEqual(3, self.dll.delete_at_head().get_data())
		self.assertEqual([], self.dll.get_elements_list())

	def test_delete_at_tail(self):
		self.dll.insert_at_tail(Node(1))
		self.assertEqual(1, self.dll.delete_at_head().get_data())
		self.assertEqual([], self.dll.get_elements_list())
		self.dll.insert_at_head(Node(5))
		self.dll.insert_at_tail(Node(1))
		self.dll.insert_at_head(Node(4))
		self.dll.insert_at_tail(Node(3))
		self.assertEqual(4, self.dll.delete_at_head().get_data())
		self.assertEqual(5, self.dll.delete_at_head().get_data())
		self.assertEqual(1, self.dll.delete_at_head().get_data())
		self.assertEqual([3], self.dll.get_elements_list())
		self.assertEqual(3, self.dll.delete_at_head().get_data())
		self.assertEqual([], self.dll.get_elements_list())

	def test_delete_at_search(self):
		self.assertEqual(-1, self.dll.search(3))
		self.dll.insert_at_tail(Node(1))
		self.assertEqual([1], self.dll.get_elements_list())
		self.assertEqual(-1, self.dll.search(3))
		self.dll.insert_at_head(Node(5))
		self.dll.insert_at_head(Node(4))
		self.dll.insert_at_tail(Node(3))
		self.assertEqual(4, self.dll.search(3))
		self.assertEqual(4, self.dll.delete_at_head().get_data())
		self.assertEqual(3, self.dll.search(3))
		self.assertEqual(5, self.dll.delete_at_head().get_data())
		self.assertEqual(2, self.dll.search(3))
		self.assertEqual(1, self.dll.delete_at_head().get_data())
		self.assertEqual(1, self.dll.search(3))
		self.assertEqual(3, self.dll.delete_at_head().get_data())
		self.assertEqual(-1, self.dll.search(3))
		


if __name__ == "__main__":
	unittest.main()



















