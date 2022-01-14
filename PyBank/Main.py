# import os
# import csv

# csvpath = os.path.join('Resource', 'budget_data.csv')
# sum = 0
# sumchg = 0

# with open(csvpath) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")

#     # Skip the header
#     next(csvreader)
#     first_row=next(csvreader)
#     value = int(first_row[1])
#     # Pass the raw text data as a list
#     csvdata = list(csvreader)
#     for row in csvdata:
#         sum = sum + int(row[1])
#         print(sum)
#         change = int(row[1]) - value
#         sumchg = sumchg + change
#         value = int(row[1]) 
    

# total_months = len(list(csvdata))
  
#     # SRead each row of data after the header

# print(sumchg)
# Avgchg = sumchg/total_months
# print("Financial Analysis")
# print("---------------------")
# print(f"Total Months: {total_months}")
# print(f"Total: {sum}")
# print(f"Average Change: {Avgchg}")

import os
import csv

csvpath = os.path.join('Resource', 'budget_data.csv')
sum = 0
sumchg = 0
months=1
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header
    next(csvreader)
    first_row=next(csvreader)
    value = int(first_row[1])
    print(value)
    sum  =int(first_row[1])
    print(sum)
    # Pass the raw text data as a list
    csvdata = list(csvreader)
    for row in csvdata:
        months = months + 1
        sum = sum + int(row[1])
        change = int(row[1]) - value
        sumchg = sumchg + change
        value = int(row[1]) 
    
total_months = len(list(csvdata))+1

  
    # SRead each row of data after the header

print(sumchg)
Avgchg = sumchg/total_months
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {total_months}")
print(f"Total: {sum}")
print(f"Average Change: {Avgchg}")


with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip over the csv file header on the first row
    next(csvreader)

    # Pass the raw text data out as a list
    csv_data = list(csvreader)
    
  
for row in csv_data:
    print(f"{row[0]:8}  {int(row[1]):14,.0f}")