from datetime import datetime, timedelta
first_date, second_date = datetime(2021, 9, 19), datetime(2021, 9, 26)
print("The original range : " + str(first_date) +  " " + str(second_date))
dates = (first_date + timedelta(idx + 1)
         for idx in range((second_date - first_date).days))
res = sum(1 for day in dates if day.weekday() < 5)
print("Total business days in range : " + str(res))
