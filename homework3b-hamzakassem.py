#get the month
month = int(input('Enter the month as an integer.'))
#validate the month
while month < 1 or month > 12: 
   print('ERROR: The month cannot be less than 1 or greater than 12.')     
   month = int(input('Enter the correct month.'))

#get the day
day = int(input('Enter the day as an integer.'))
#validate the day
while day < 1 or day > 31:
   print('ERROR: The day cannot be less than 1 or greater than 31.')
   day = int(input('Enter the correct day.'))

#get the year
year = int(input('Enter the year as an integer.'))
#validate the year
while year < 0 or year > 99:
   print('ERROR: The year cannot be less than 00 or greater than 99.')
   year = int(input('Enter the correct year.'))

#determine if the date is magic or not
if year == month * day:
   print('Magic Date')
else:
   print('Not a Magic Date')    
