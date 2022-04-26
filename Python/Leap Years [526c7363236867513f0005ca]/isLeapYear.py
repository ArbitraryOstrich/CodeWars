def isLeapYear(year):
    if year%4 == 0 and not year%100 == 0:
        return True
    else:
        if year%400 == 0:
                return True
    return False
