import unittest

class Node:

	def __init__(self, data=None, next=None):
		self._data = data
		self._next = next

	def setNext(self, node):
		self._next = node

	def getNext(self):
		return self._next

	def setData(self, data):
		self._data = data

	def getData(self):
		return self._data

class LinkedList:
	
	def __init__(self, head=None):
		self._head = head

	def insert_at_head(self, node):
		# takes constant time, O(1)
		node.setNext(self._head)
		self._head = node

	def insert_at_tail(self, node):
		# takes linear time, O(n)
		if self._head is None:
			self._head = node
		else:
			curr = self._head
			# traverse linkedlist until we reach last element
			while curr.getNext():
				curr = curr.getNext()

			curr.setNext(node)

	def delete_at_head(self):
		# takes constant time, O(1)
		if self._head:
			self._head = self._head.getNext()

	def delete_at_tail(self):
		# takes constant time, O(n)
		if self._head:
			if self._head.getNext():
				curr = self._head
				# traverse linkedlist until we reach
				# last but one node
				while curr.getNext().getNext():
					curr = curr.getNext()

				curr.setNext(None)
			else:
				self._head = None

	def search(self, value):
		# search for a node with data=value and return the
		# index of that node. First node's index is 1 and so on.
		# if node is not found, return -1
		
		if not self._head:
			return -1

		if self._head.getData() == value:
			return 1

		counter = 1
		current = self._head

		# traverse linkedlist until we find the node
		# or we reach end of linkedlist in which case
		# return -1
		while current:
			if current.getData() == value:
				return counter

			counter += 1
			current = current.getNext()

		return -1


	def get_elements_list(self):
		# returns an array with element as node's data
		# from head to tail
		curr = self._head
		elements = []

		while curr:
			elements.append(curr.getData())
			curr = curr.getNext()

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
		self.ll.delete_at_head()
		self.ll.delete_at_head()
		self.assertEqual([3,4,5], self.ll.get_elements_list())
		self.ll.delete_at_head()
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
		self.ll.delete_at_tail()
		self.ll.delete_at_tail()
		self.assertEqual([1,2,3], self.ll.get_elements_list())
		self.ll.delete_at_tail()
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
		self.ll.delete_at_tail()
		self.ll.delete_at_tail()
		self.assertEqual(-1, self.ll.search(4))
		self.ll.delete_at_tail()
		self.assertEqual(2, self.ll.search(2))

if __name__ == "__main__":
	unittest.main()