import calendar
from datetime import date

def MeetupDayException(Exception):
	pass

def meetup_day(year, month, day_of_the_week, which):
	week={1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}
	if month==2 :
		if calendar.isleap(year):
			end = 29
		else:
			end=28
	else:
		end=calendar.monthrange(year,month)[1]+1
	if which=='teenth':
		for i in range(13,20):
			if day_of_the_week==week[date(year, month, i).isoweekday()]:
				dat=i
				break

	elif which=='1st':
		for i in range(1,end):
			if day_of_the_week==week[date(year, month, i).isoweekday()]:
				dat=i
				break
	elif which=='2nd':
		count=2
		for i in range(1,end):
			if day_of_the_week==week[date(year, month, i).isoweekday()]:
				count-=1
				if count==0:
					dat=i
					break
	elif which=='3rd':
		count=3
		for i in range(1,end):
			if day_of_the_week==week[date(year, month, i).isoweekday()]:
				count-=1
				if count==0:
					dat=i
					break
	elif which=='4th':
		count=4
		for i in range(1,end):
			if day_of_the_week==week[date(year, month, i).isoweekday()]:
				count-=1
				if count==0:
					dat=i
					break
	elif which=='5th':
		count=5
		for i in range(1,end):
			if day_of_the_week==week[date(year, month, i).isoweekday()]:
				count-=1
				if count==0:
					dat=i
					break
	elif which=='last':
		for i in range(end-1,0,-1):
			if day_of_the_week==week[date(year, month, i).isoweekday()]:
				dat=i
				break
	if type(dat) is None:
		raise MeetupDayException('No such day found')
		
	return (date(year,month,dat))

	