import unittest

def power(x, n):
	if n==0:
		return 1
	elif n%2==0:
		return power(x, n/2) * power(x, n/2)
	else:
		return power(x, n/2) * power(x, n/2) * x


class TestPower(unittest.TestCase):

	def test_power_1(self):
		x = 2
		n = 5
		answer = 32
		self.assertEqual(answer, power(x, n))

	def test_power_2(self):
		x = 2
		n = 0
		answer = 1
		self.assertEqual(answer, power(x, n))

	def test_power_3(self):
		x = -2
		n = 5
		answer = -32
		self.assertEqual(answer, power(x, n))

	def test_power_4(self):
		x = 0
		n = 10
		answer = 0
		self.assertEqual(answer, power(x, n))

	def test_power_5(self):
		x = 2
		n = 10
		answer = 1024
		self.assertEqual(answer, power(x, n))

	def test_power_6(self):
		x = -3
		n = 4
		answer = 81
		self.assertEqual(answer, power(x, n))


# You can run all testcases by navigating to this directory
# and run "python binary_search.py"
if __name__ == "__main__":
	unittest.main()