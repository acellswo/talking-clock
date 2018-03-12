
class ConvertTimeToSpoken():		
	@staticmethod
	def convert(time):
		if not(is_valid_time(time)):
			return "";
		
		return "It's one thirteen am";
	
def is_valid_time(time):
	if time is None \
	or not(isinstance(time, str)) \
	or len(time) != 5 \
	or time[2] != ":" \
	:
	# TODO: check that all chars are digits
		return False
	
	return True