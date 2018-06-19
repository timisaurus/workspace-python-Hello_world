import time

n = time.time()

n_days = n / 60 / 60 / 24
int_n_days = int(n_days)
n_hours = (n_days - int_n_days) * 24
int_n_hours = int(n_hours)
n_minutes = (n_hours - int_n_hours) * 60
int_n_minutes = int(n_minutes)
n_seconds = (n_minutes - int_n_minutes) * 60
int_n_seconds = int(n_seconds)

int_n_days_seconds = int_n_days * 60 * 60 * 24
int_n_hours_seconds = int_n_hours * 60 * 60
int_n_minutes_seconds = int_n_minutes * 60

special_snowflake = n - (int_n_days_seconds + int_n_hours_seconds + int_n_minutes_seconds)

int_special_snowflake = int(special_snowflake)

print(int_n_days, 'days', int_n_hours, 'hours', int_n_minutes,
      'minutes', int_special_snowflake, 'seconds')

'''
while True:
    print('hi')

n = int(input())

if n == n < 0 or n > 168:
    print ('INVALID')
elif n <= 40:
    n = n * 8
    print ('YOU MADE', n ,'DOLLARS THIS WEEK')
elif n <= 50:
    n = n - 40
    n = (n * 9) + 320
    print ('YOU MADE', n ,'DOLLARS THIS WEEK')
elif n > 50:
    n = n - 50
    n = (n * 10) + 410
    print ('YOU MADE', n ,'DOLLARS THIS WEEK')



n = int(input('seconds:'))

n_days = n/60/60/24
int_n_days = int(n_days)
n_hours = (n_days - int_n_days) * 24
int_n_hours = int(n_hours)
n_minutes = (n_hours - int_n_hours) * 60
int_n_minutes = int(n_minutes)
n_seconds = (n_minutes - int_n_minutes) * 60
int_n_seconds = int(n_seconds)

int_n_days_seconds = int_n_days*60*60*24
int_n_hours_seconds = int_n_hours*60*60
int_n_minutes_seconds = int_n_minutes*60

special_snowflake = n - (int_n_days_seconds+int_n_hours_seconds+int_n_minutes_seconds)

int_special_snowflake = int(special_snowflake)

print (int_n_days, 'days', int_n_hours, 'hours', int_n_minutes,
      'minutes', int_special_snowflake, 'seconds')

'''
