# Given your birthday and the current date, calculate your age
# in days. Compensate for leap days. Assume that the birthday
# and current date are correct dates (and no time travel).
# Simply put, if you were born 1 Jan 2012 and todays date is
# 2 Jan 2012 you are 1 day old.

# 0 Don't Panic!
# 1 What are the inputs?
# 2 What are the outputs?
# 3 Work Some examples by hand.
# 4 Simple mechanical solution.
# 5 Develop incrementally and test as we go.


# IMPORTANT: You don't need to solve the problem yet!
# Just brainstorm ways you might approach it!

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def isLeapYear(year):
    if year % 4 == 0:
        return True
    else:
        if year % 100 == 0:
            return False
        else:
            if year % 400 == 0:
                return True
            else:
                return False

def daysUntilMonth(m1):
    monthIndex = 0
    totalDaysUpUntilm1 = 0
    while monthIndex < m1 - 1:
        totalDaysUpUntilm1 += daysOfMonths[monthIndex]
        monthIndex += 1
    return totalDaysUpUntilm1

def daysUntilYear(y1):
    yearIndex = 0
    totalDaysUpUntily1 = 0
    while yearIndex < y1:
        if isLeapYear(yearIndex):
            totalDaysUpUntily1 += 366
            yearIndex += 1
        else:
            totalDaysUpUntily1 += 365
            yearIndex += 1
    return totalDaysUpUntily1

def dateInDays(y1, m1, d1):
    total = d1 + daysUntilMonth(m1) + daysUntilYear(y1)
    # if leap year
    if isLeapYear(y1) == True and m1 > 2:
        total += 1
    return total

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    return dateInDays(y2,m2,d2) - dateInDays(y1,m1,d1)

print isLeapYear(2012)
