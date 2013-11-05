import datetime as dt

def dayofweek():
    days=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    dateToday=dt.date.today()

    dayofWeek=dateToday.weekday()
    
    return days[dayofWeek]

def birthday(birthdate):

    t=birthdate.split('/')
    
    bday=dt.date(int(t[2]), int(t[1]), int(t[0]))
    dateToday=dt.date.today()

    age=dateToday-bday
    ageDays=age.days

    year_rest=divmod(ageDays, 365)
    years=year_rest[0]
    months_rest=divmod(year_rest[1], 30)
    months=months_rest[0]
    days=months_rest[1]

    age=(years, months, days)

    bdaytuple=(bday.month, bday.day)
    dateTodayTuple=(dateToday.month, dateToday.day)

    if bdaytuple<dateTodayTuple:
        nextbday=bday.replace(year=dateToday.year+1)

    else:
        nextbday=bday.replace(year=dateToday.year)

    timeLeft=nextbday-dateToday

    return [age, timeLeft]

def doubleday(bd1, bd2):


    t1a=bd1.split('/')
    t2a=bd2.split('/')

    BDay1=dt.date(int(t1a[2]), int(t1a[1]), int(t1a[0]))
    BDay2=dt.date(int(t2a[2]), int(t2a[1]), int(t2a[0]))

    if BDay1>BDay2:
        t1=BDay1
        t2=BDay2
    else:
        t2=BDay1
        t1=BDay2

    age2_start=t1-t2

    age2Days=age2_start.days

    age1Days=0

    i=0

    while age2Days!=2*age1Days:
        
        i+=1

        age1Days+=1
        age2Days+=1


    occurs=t1+dt.timedelta(i)

    return occurs

def general_day(bd1, bd2, n=2):


    t1a=bd1.split('/')
    t2a=bd2.split('/')

    BDay1=dt.date(int(t1a[2]), int(t1a[1]), int(t1a[0]))
    BDay2=dt.date(int(t2a[2]), int(t2a[1]), int(t2a[0]))

    if BDay1>BDay2:
        t1=BDay1
        t2=BDay2
    else:
        t2=BDay1
        t1=BDay2

    age2_start=t1-t2

    age2Days=age2_start.days

    age1Days=0

    i=0

    while age2Days!=n*age1Days:
        
        i+=1

        age1Days+=1
        age2Days+=1


    occurs=t1+dt.timedelta(i)

    return occurs

if __name__ == '__main__':
    #------------------
    #Part 1 Test Code
    #------------------
    # print dayofweek()


    #---------------------
    #Part 2 Test Code
    #---------------------

    bday=raw_input("Please Enter Your Date of Birth (DD/MM/YYY): ")

    timeleft=birthday(bday)
    print "Your age is ", timeleft[0][0], "years, ", timeleft[0][1], "months and ", timeleft[0][2], "days. There are ", timeleft[1], "until your next birthday"


    #--------------------
    #Part 3 Test Code
    #--------------------

    # bday1=raw_input("Please Enter the First Person's Date of Birth (DD/MM/YYY): ")
    # bday2=raw_input("Please Enter the Second Person's Date of Birth (DD/MM/YYY): ")
    # res=doubleday(bday1, bday2)

    # print "The date of your DoubleDay is/was: ", res

    #--------------------
    #Part 4 Test Code
    #--------------------

    # bday1=raw_input("Please Enter the First Person's Date of Birth (DD/MM/YYY): ")
    # bday2=raw_input("Please Enter the Second Person's Date of Birth (DD/MM/YYY): ")
    # n=raw_input("What age gap would you like to calculate (e.g. one is twice as old or three times as old etc.)? ")
    # #print int(n)
    # res=general_day(bday1, bday2, int(n))

    # print "The date at which your chosen age gap will occur/has occired: ", res