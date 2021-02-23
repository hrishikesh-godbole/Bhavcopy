# importing datetime module 

import datetime
from datetime import date
import calendar
from nsepy.history import get_price_list

#Taking date as input from the user
d1, m1, y1 = [int(x) for x in input("Enter date(DD/MM/YYYY) : ").split('/')] 

b1 = date(y1, m1, d1) 


# Check the dates
if b1.weekday() == 6:
    print("Bhavcopy isn't available on sundays")

elif b1 == date.today():
    prices = get_price_list(dt = date.today())
    prices.to_csv('bhavcopy.csv')
	
elif b1 < date.today():
    prices = get_price_list( dt = datetime.datetime(int(y1),int(m1),int(d1)))
    prices.to_csv('bhavcopy.csv')
    
else:
    print("Entered date is future date") 
