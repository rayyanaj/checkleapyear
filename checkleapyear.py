def IsLeap(year):  
  # Checking if the given year is leap year  
  if((year % 400 == 0) or # to check whether century year is leap year or  
     (year % 100 != 0) and # to check whether it's a century year or not
     (year % 4 == 0)):   # to check whether any year is leap year
    print(year, "is a leap year");  
  # Else it is not a leap year  
  else:  
    print (year, "is not a leap year")  
# Taking an input year from user  
year = int(input("Enter the year: "))  
  
# Printing result  
IsLeap(year)
