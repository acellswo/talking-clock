from spoken_number import spoken_number

class ConvertTimeToSpoken():		
	invalid_input_message = "Invalid input";
	
	def convert(time):
		if not(is_valid_time(time)):
			return ConvertTimeToSpoken.invalid_input_message;
		
		hours = None
		hours = time[0:-3]
		minutes = time[3:]	
		
		if not(hours.isdigit() and minutes.isdigit()):
			return ConvertTimeToSpoken.invalid_input_message;
		
		hours_int = int(hours)
		minutes_int = int(minutes)
		assert hours != None
		assert minutes != None
		
		if not(hours_int < 24 and hours_int >= 0) \
			or not(minutes_int < 60 and minutes_int >= 0):
			return ConvertTimeToSpoken.invalid_input_message;
		
		if hours_int < 12:
			spoken_am = "am"
		else:
			spoken_am = "pm"
		
		#hours special cases
		if (hours_int == 0):
			spoken_hours = "twelve"
		else:
			if (hours_int > 12):
				spoken_hours = spoken_number.get_spoken(str(hours_int - 12))
			else:
				spoken_hours = spoken_number.get_spoken(hours)
				
		#minutes special cases
		if (minutes_int == 0):
			return "It's {} {}".format(spoken_hours, spoken_am)
		elif minutes_int < 10:
			spoken_mintues = "oh " + spoken_number.get_spoken(minutes)
		else:
			spoken_mintues = spoken_number.get_spoken(minutes)
			
		return "It's {} {} {}".format(spoken_hours, spoken_mintues, spoken_am)
	
def is_valid_time(time):
	if time is None \
	or not(isinstance(time, str)) \
	or len(time) != 5 \
	or time[2] != ":" \
	:
		return False
	
	return True