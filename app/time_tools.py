


def second_converter(l):
    l = l.split(':')
    l.reverse()
    s = 0
    for e,v in zip(l,[1,60,3600,86400]):
        s += int(e)*v
    return(s)


def sum_duration(duration_array):

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