from datetime import date

from nsepy.history import get_price_list
prices = get_price_list(dt = date(2021,2,1))

prices.to_csv('bhavcopy.csv')