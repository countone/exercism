import datetime
def add_gigasecond(birth_date):
	seconds = birth_date.timestamp()
	seconds+=1000000000
	return datetime.datetime.fromtimestamp(seconds)
