def findDayDiff(month1,day1,month2,day2):
    Jan = 0
    Feb = Jan+31
    Mar = Feb+28
    Apr = Mar+31
    May = Apr+30
    Jun = May+31
    Jul = Jun+30
    Aug = Jul+31
    Sep = Aug+31
    Oct = Sep+30
    Nov = oct+31
    dec = nov +30




def time_delta(t1, t2):
    splittedDate = t1.split(" ")
    date1 = int(splittedDate[1])
    month1 = splittedDate[2]
    year1 = int(splittedDate[3])
    splitedTime = splittedDate[4].split(":")
    hour1 = int(splitedTime[0])
    minute1 = int(splitedTime[1])
    second1 = int(splitedTime[2])
    gst1 = int(splittedDate[5])


    splittedDate = t1.split(" ")
    date2 = int(splittedDate[1])
    month2 = int(splittedDate[2])
    year2 = int(splittedDate[3])
    splitedTime = splittedDate[4].split(":")
    hour2 = int(splitedTime[0])
    minute2 = int(splitedTime[1])
    second2 = int(splitedTime[2])
    gst2 = int(splittedDate[5])

    secDif = second2 - second1
    print("second Difference"),
    print(secDif)

    minDif = minute2 - minute1
    print("minute Difference"),
    print(minDif)

    #dayDif = findDayDiff(month1,date1,month2,date2)
    dayDiff = 0

    yearDif = year2 - year1
    print("year difference"),
    print(yearDif)

    gst = gst2 - gst1
    print("gst Diff"),
    print(gst)

    seconsDifference = secDif + minDif*60 + hrDif*60*60 + dayDif*24*60*60 + yearDif*360*24*60*60 +gstDif
    print("season Difference"),
    print(seconsDifference)


time_delta("Sun 10 May 2015 13:54:36 -0700","Sun 10 May 2015 13:54:36 -0000")