# leap year or not
def is_leap_year(year):
    """
    docstring: this is_leap_year fn gives us a year is leap year or not
    """
    
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False
    
    
    
output_is_leap_year = is_leap_year(int(input("Enter Your Year: ")))
print(output_is_leap_year)