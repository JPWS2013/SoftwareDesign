import datetime as dt

def dayofweek():
	days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

	dateToday=dt.date.today()

	dayofWeek=dateToday.weekday()
	
	return days[dayofWeek]

def birthday(birthdate):

	t=birthdate.split('/')
	
	BDay=dt.date(int(t[2]), int(t[1]), int(t[0]))
	dateToday=dt.date.today()

	age=dateToday-BDay
	ageDays=age.days

	year_rest=divmod(ageDays, 365)
	years=year_rest[0]
	months_rest=divmod(year_rest[1], 30)
	months=months_rest[0]
	days=months_rest[1]

	age=(years, months, days)

	BDaytuple=(BDay.month, BDay.day)
	dateTodayTuple=(dateToday.month, dateToday.day)

	if BDaytuple<dateTodayTuple:
		nextBDay=BDay.replace(year=dateToday.year+1)

	else:
		nextBDay=BDay.replace(year=dateToday.year)

	timeLeft=nextBDay-dateToday

	return [age, timeLeft]

def doubleday(bd1, bd2):

	t1a=bd1.split('/')
	t2a=bd2.split('/')

	if t1a>t2a:
		t1=t1a
		t2=t2a
	else:
		t2=t1a
		t1=t2a

	print t1, t2

	BDay1=dt.date(int(t1[2]), int(t1[1]), int(t1[0]))
	BDay2=dt.date(int(t2[2]), int(t2[1]), int(t2[0]))
	dateToday=dt.date.today()

	age1=dateToday-BDay1
	age2=dateToday-BDay2

	age1Days=age1.days
	age2Days=age2.days

	i=1

	while age2Days!=2*age1Days:
		age1Days+=1
		age2Days+=1

		print "age1Days=", age1Days
		print "age2Days=", age2Days

		if age2Days==2*age1Days:
			break
		i+=1
		print i

	return i


if __name__ == '__main__':

	#print dayofweek()

	# bday=raw_input("Please Enter Your Date of Birth (DD/MM/YYY): ")

	# timeleft=birthday(bday)
	# print "Your age is ", timeleft[0][0], "years, ", timeleft[0][1], "months and ", timeleft[0][2], "days. There are ", timeleft[1], "until your next birthday"

	print doubleday('06/09/1974', '26/02/1994')