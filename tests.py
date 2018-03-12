import unittest
from converter import ConvertTimeToSpoken

class TestTimeConversionOutputs(unittest.TestCase):

	def test_simple_am_time_test(self):
		input = "01:13"
		expectedOutput = "It's one thirteen am"
		
		actualOutput = ConvertTimeToSpoken.convert(input);
		
		self.assertEqual(expectedOutput, actualOutput)
		
	def test_pm_time_test(self) :
		input = "13:45"
		expectedOutput = "It's one forty five pm"
		
		actualOutput = ConvertTimeToSpoken.convert(input);
		self.assertEqual(expectedOutput, actualOutput)

	def test_reddit_tests(self):
		inputs = ["00:00", "01:30", "12:05", "14:01", "20:29", "21:00"]
		expectedOutput = ["It's twelve am", "It's one thirty am", "It's twelve oh five pm", "It's two oh one pm", "It's eight twenty nine pm", "It's nine pm"]
		
		self.assertEqual(len(inputs), len(expectedOutput))
		
		for i in range(0, len(inputs)):
			actualOutput = ConvertTimeToSpoken.convert(inputs[i]);
			self.assertEqual(expectedOutput[i], actualOutput)
			
	def test_invalid_input(self):
		expectedOutput = "Invalid input"
		
		input = ""
		assert_expected(self, input, expectedOutput)
		
		input = "asfasdgasggggggg"
		assert_expected(self, input, expectedOutput)
		
		input = "as:f&"
		assert_expected(self, input, expectedOutput)
		
		input = "1:23"
		assert_expected(self, input, expectedOutput)
		
		input = "12/34"
		assert_expected(self, input, expectedOutput)
		
def assert_expected(self, input, expectedOutput):
	actualoutput = ConvertTimeToSpoken.convert(input)
	return self.assertEqual(expectedOutput, actualoutput)