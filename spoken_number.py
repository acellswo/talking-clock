class spoken_number() :
	simple_lookup = {
		0: "zero",
        1: "one",
		2: "two",
		3: "three",
		4: "four",
		5: "five",
		6: "six",
		7: "seven",
		8: "eight",
		9: "nine",
		10: "ten",
		11: "eleven",
		12: "twelve",
		13: "thirteen",
		14: "fourteen",
		15: "fifteen",
		16: "sixteen",
		17: "seventeen",
		18: "eighteen",
		19: "nineteen",
    }
	
	tens_lookup = {
		# <20 is specially handled
		2: "twenty",
		3: "thirty", 
		4: "forty",
		5: "fifty", 
		6: "sixty", 
		7: "seventy",
		8: "eighty",
		9: "ninety"
	}
	
	def get_spoken(number_as_str):
		number = int(number_as_str)
		assert number < 100
		
		tens = int(number / 10)
		ones = int(number % 10)
		
		default_val = "derp"
		spoken = spoken_number.simple_lookup.get(number, default_val)
		wasFound = spoken != default_val
		
		if wasFound:
			return spoken
		else: 
			spoken_tens = spoken_number.tens_lookup.get(tens, default_val)
			#this should always find something in the lookups
			assert spoken_tens != default_val
			
			if ones != 0:
				spoken_ones = spoken_number.simple_lookup.get(ones, default_val)
				assert spoken_ones != default_val
				return spoken_tens + " " + spoken_ones
			else:
				return spoken_tens