import unittest

class Stack:

	def __init__(self):
		self._arr = []
		self._top = -1

	def push(self, obj):
		self._top += 1
		self._arr.append(obj)

	def pop(self):
		# raise exception if stack is empty
		if self._top < 0:
			raise Exception("Stack is empty")

		elem = self._arr.pop()
		self._top -= 1

		return elem

	def top(self):
		# raise exception if stack is empty
		if self._top < 0:
			raise Exception("Stack is empty")

		return self._arr[self._top]



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