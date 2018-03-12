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
		
		assert hours != None
		assert int(hours) < 24 and int(hours) >= 0 
		#todo: invalid input return
		
		minutes = time[3:4]
		assert minutes != None 
		assert int(minutes) < 60 and int(minutes) >= 0
		
		if int(hours) < 12:
			spoken_am = "am"
		else:
			spoken_am = "pm"
		
		spoken_hours = spoken_number.get_spoken(hours)
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