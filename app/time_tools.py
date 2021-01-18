# Collection of function to add durations in the format HH:MM:SS
# Needed to compute duration such as 26:05:30



def second_converter(time_string):
	"""
	Second Converter

		Convert string timecode to int value (in seconds)

	Args:

		time_string: a string timecode in the format HH:MM:SS

	Returns:

		s: an int value equivalent to the number of seconds in the input strings.


	"""
	
    time_string = time_string.split(':')
    time_string.reverse()
    s = 0
    for e,v in zip(time_string,[1,60,3600,86400]):
        s += int(e)*v
    return(s)


def sum_duration(duration_array):
	"""
	Sum Duration

		Sums up all the timecode in the input array and return the sum as a timecode

	Args:

		duration_array: an array containing string timecodes in the format HH:MM:SS

	Returns:

		final_string: the string timecode sum of the timecodes array in the format HH:MM:SS

	"""

	total = sum(list(map(second_converter,duration_array)))
	hour = total//3600
	total = total%3600
	minute = total//60
	second =  total%60

	H = str(hour)
	M = str(minute).zfill(2)
	S = str(second).zfill(2)

	final_string = ':'.join([H,M,S])

	return(final_string)