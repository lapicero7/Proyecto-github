def isYearLeap(year):

#

    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


#

 

def daysInMonth(year, month):

#

    if month < 1 or month > 12:
        return None
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2:
        if isYearLeap(year):
            return 29
        else:
            return 28
    return months[month-1]


#

 

def dayOfYear(year, month, day):

#

    
    if month < 1 or month > 12 or day < 1 or day > 31:
        return None
    days = 0
    for i in range(1, month):
        days_in_month = daysInMonth(year, i)
        if days_in_month is None:
            return None
        days += days_in_month
    days += day
    return days



#
print(dayOfYear(2000, 12, 31))
testYears = [1900, 2000, 2016, 1987]

testMonths = [2, 2, 1, 11]

testResults = [28, 29, 31, 30]

for i in range(len(testYears)):

                yr = testYears[i]

                mo = testMonths[i]

                print(yr, mo, "->", end="")

                result = daysInMonth(yr, mo)

                if result == testResults[i]:

                               print("OK")

                else:

                               print("Failed")




