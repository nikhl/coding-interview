import unittest

from doubly_linked_list import DoublyLinkedList, Node

class Queue:

	def __init__(self):
		self._dll = DoublyLinkedList()

	def enqueue(self, data):
		self._dll.insert_at_head(Node(data))

	def dequeue(self):
		elem = self._dll.delete_at_tail()
		if not elem:
			raise Exception("Queue is empty")

		return elem.get_data()

class TestQueue(unittest.TestCase):

	def setUp(self):
		self.queue = Queue()

	def test_enqueue(self):
		self.queue.enqueue(1)
		self.queue.enqueue(2)
		self.queue.enqueue(3)
		self.assertEqual(1, self.queue.dequeue())
		self.assertEqual(2, self.queue.dequeue())
		self.assertEqual(3, self.queue.dequeue())
		self.assertRaises(Exception, self.queue.dequeue)

	def test_dequeue(self):
		self.assertRaises(Exception, self.queue.dequeue)
		self.queue.enqueue(1)
		self.assertEqual(1, self.queue.dequeue())
		self.assertRaises(Exception, self.queue.dequeue)
		self.queue.enqueue(2)
		self.queue.enqueue(3)
		self.assertEqual(2, self.queue.dequeue())
		self.assertEqual(3, self.queue.dequeue())
		self.assertRaises(Exception, self.queue.dequeue)

if __name__ == "__main__":
	unittest.main()
