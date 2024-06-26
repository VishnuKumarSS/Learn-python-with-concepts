def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return True # true means leapyear
      else:
        return False # false means not leap year
    else:
      return True
  else:
    return False

def days_in_month(year,month):
    if month > 12 or month < 1:
        return ("Invalid month")
    #print(is_leap(year))
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
    if is_leap(year) is True:
        month_days[1]=29
    #print(month_days)
    return month_days[month-1]

  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)

