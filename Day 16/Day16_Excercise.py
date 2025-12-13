# Get the current day, month, year, hour, minute and timestamp from datetime module

from datetime import datetime
now=datetime.now()
print(now.day)
print(now.month)
print(now.year)
print(now.hour)
print(now.minute)
print(now.second)
print(now.timestamp())

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

from datetime import datetime
now=datetime.now()
t=now.strftime('%m/%d/%Y,%H:%M:%S')
print(t)

# Today is 5 December, 2019. Change this time string to time.

date='5 December 2019'
time=datetime.strptime(date,'%d %B %Y')
print(time)

# Calculate the time difference between now and new year.

from datetime import date
now=date(year=2025,month=12,day=13)
new_year=date(2026,1,1)
diff=new_year-now
print(f'Time left for new year is :{diff}')

# Calculate the time difference between 1 January 1970 and now.

from datetime import date
dates=date(year=1970,month=1,day=1)
now= date.today()
diff=now-dates
print(f'Time difference is :{diff}')

# Think, what can you use the datetime module for?

# Time series analysis
# To get a timestamp of any activities in an application
# Adding posts on a blog
# Checking reminders and stuff
# Tracking app usage
# Token expiration and sessions
