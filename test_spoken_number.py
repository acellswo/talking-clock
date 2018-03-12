import unittest
from spoken_number import spoken_number

class TestSpokenNumberConversions(unittest.TestCase):

	def test_single_digit_num(self):
		result = spoken_number.get_spoken("5")
		self.assertEqual("five", result)
	
	def test_13(self):
		result = spoken_number.get_spoken("13")
		self.assertEqual("thirteen", result)
	
	def test_49(self):
		result = spoken_number.get_spoken("49")
		self.assertEqual("forty nine", result)
		
	def test_0(self):
		result = spoken_number.get_spoken("0")
		self.assertEqual("zero", result)
		
	def test_oh(self):
		result = spoken_number.get_spoken("0000003")
		self.assertEqual("three", result)
		
	def test_30(self):
		result = spoken_number.get_spoken("30")
		self.assertEqual("thirty", result)
		
	def test_1000(self):
		with self.assertRaises(AssertionError):
			spoken_number.get_spoken("1000")
			