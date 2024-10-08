def leap_year(year):

    # VERIFY IF IS LEAP YEAR!
    if year % 100 == 0:
       return True # YEAR LEAP
    else:
        if year % 400 == 0 and year % 100 == 0:
           return True
        else:
            return False

year_val = 1992

print(leap_year(year_val))
