import os
import csv

csvpath = os.path.join('Resource', 'budget_data.csv')

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header
    next(csvreader)
    csvdata = list(csvreader)
   
    min_month = None
    max_month = None
    cum_pl = 0
    for idx, (month, pl) in csvdata:
     new_cum_pl = cum_pl + pl
     if new_cum_pl < cum_pl:
       min_month = month
     if new_cum_pl > cum_pl:
       max_month = month
     cum_pl = new_cum_pl
    print(min_month)

   # your new total months is idx+1, min_month is stored, max_month is stored, cumulative pl is in cum_pl
   # this is computer optimized. i.e you read the csv only once

