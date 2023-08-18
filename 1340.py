import datetime
date_format ='%B %d, %Y %H:%M'
date_obj = datetime.datetime.strptime(input(), date_format)
total_year_datetime = datetime.datetime(year=date_obj.year, month=12, day=31) - datetime.datetime(year=date_obj.year-1, month=12, day=31)
input_year_datetime = date_obj - datetime.datetime(year=date_obj.year, month=1, day=1)
print(round(input_year_datetime/total_year_datetime*100,15))