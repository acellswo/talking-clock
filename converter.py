from spoken_number import spoken_number

class ConvertTimeToSpoken():		
	@staticmethod
	def convert(time):
		if not(is_valid_time(time)):
			return "Invalid input";
		#todo: invalid digits
		
		#hours
		hours = None
		if time[0] == "0":
			# must ignore leading 0 for hours
			hours = time[1]
		else: 
			hours = time[0:1]
		
		hours_int = int(hours)
		assert hours != None
		assert hours_int < 24 and hours_int >= 0 
		#todo: invalid input return
		
		minutes = time[3:4]
		minutes_int = int(minutes)
		assert minutes != None 
		assert minutes_int < 60 and minutes_int >= 0
		
		if hours_int < 12:
			spoken_am = "am"
		else:
			spoken_am = "pm"
		
		if (hours_int == 0):
			spoken_hours = "twelve"
		else:
			if (hours_int > 12):
				spoken_hours = spoken_number.get_spoken(str(hours_int - 12)
			else 
				spoken_hours = spoken_number.get_spoken(hours)
				
		if (minutes_int == 0):
			spoken_mintues = ""
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