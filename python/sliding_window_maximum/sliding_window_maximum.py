import unittest
import collections


def sliding_window_max(arr, k):

	if len(arr) < k:
		return None

	result = []
	index_deque = collections.deque()
	index_deque.append(0)

	for i in xrange(1,k):
		curr = arr[i]
		while index_deque:
			if curr > arr[index_deque[0]]:
				index_deque.popleft()
			else:
				break

		index_deque.appendleft(i)

	for i in xrange(k,len(arr)):
		result.append(arr[index_deque[-1]])
		if (i-k) >= index_deque[-1]:
			index_deque.pop()

		while index_deque:
			if arr[i] > arr[index_deque[0]]:
				index_deque.popleft()
			else:
				break

		index_deque.appendleft(i)

	result.append(arr[index_deque[-1]])
	return result


class TestSlidingWindowMax(unittest.TestCase):

	def test_sliding_window_max_1(self):
		arr = [1,3,-1,-3,5,3,6,7]
		result = [3,3,5,5,6,7]
		window_size = 3
		self.assertEqual(result, sliding_window_max(arr, window_size))

	def test_sliding_window_max_2(self):
		arr = [11,4,9,15,6,3,4,5]
		result = [11,4,9,15,6,3,4,5]
		window_size = 1
		self.assertEqual(result, sliding_window_max(arr, window_size))

	def test_sliding_window_max_3(self):
		arr = [11,4,9,15,6,3,4,5]
		result = [11,9,15,15,6,4,5]
		window_size = 2
		self.assertEqual(result, sliding_window_max(arr, window_size))

if __name__ == "__main__":
	unittest.main()