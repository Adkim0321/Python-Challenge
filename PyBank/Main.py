import os
import csv

csvpath = os.path.join('Resource', 'budget_data.csv')

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header
    next(csvreader)

    # Pass the raw text data as a list
    csvdata = list(csvreader)

total_months = len(list(csvdata))
  
    # SRead each row of data after the header
sum = 0
for row in csvdata:
    sum = sum + int(row[1])
    Avg = int(row[1]) - sum 
    print(Avg)
Avgchg = Avg/total_months
print(Avgchg)
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {total_months}")
print(f"Total: {sum}")

   

   # Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578 
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

