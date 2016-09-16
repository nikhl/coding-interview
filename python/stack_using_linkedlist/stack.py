import unittest

# use LinkedList and Node from
# https://github.com/nikhl/coding_interview/tree/master/python/linked_list
import linked_list

class Stack:

	def __init__(self):
		self._ll = linked_list.LinkedList()

	def push(self, data):
		node = linked_list.Node(data)
		self._ll.insert_at_head(node)

	def pop(self):
		# raise exception if stack is empty
		if not self.top():
			raise Exception("Stack is empty")

		elem = self._ll.delete_at_head()
		if elem:
			return elem.get_data()

		return None

	def top(self):
		# raise exception if stack is empty
		if not self._ll.get_head():
			raise Exception("Stack is empty")

		return self._ll.get_head().get_data()



class TestStack(unittest.TestCase):

	def setUp(self):
		self.stack = Stack()

	def test_stack_push(self):
		self.stack.push(1)
		self.assertEqual(1, self.stack.top())
		self.stack.push(2)
		self.stack.push(3)
		self.stack.push(4)
		self.stack.push(5)
		self.assertEqual(5, self.stack.top())
		self.stack.pop()
		self.stack.pop()
		self.assertEqual(3, self.stack.top())
		self.stack.push(5)
		self.assertEqual(5, self.stack.top())

	def test_stack_pop(self):
		self.assertRaises(Exception, self.stack.pop)
		self.stack.push(1)
		self.assertEqual(1, self.stack.pop())
		self.stack.push(2)
		self.stack.push(3)
		self.stack.push(4)
		self.stack.push(5)
		self.assertEqual(5, self.stack.pop())
		self.stack.pop()
		self.stack.pop()
		self.assertEqual(2, self.stack.pop())
		self.stack.push(5)
		self.assertEqual(5, self.stack.pop())
		self.assertRaises(Exception, self.stack.pop)

	def test_stack_top(self):
		self.assertRaises(Exception, self.stack.top)
		self.stack.push(1)
		self.assertEqual(1, self.stack.pop())
		self.stack.push(2)
		self.stack.push(3)
		self.stack.push(4)
		self.stack.push(5)
		self.assertEqual(5, self.stack.top())
		self.stack.pop()
		self.stack.pop()
		self.assertEqual(3, self.stack.top())
		self.stack.push(5)
		self.assertEqual(5, self.stack.top())
		self.stack.pop()
		self.stack.pop()
		self.stack.pop()
		self.assertRaises(Exception, self.stack.top)

if __name__ == "__main__":
	unittest.main()