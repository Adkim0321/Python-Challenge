import os
import csv

csvpath = os.path.join('Resource', 'budget_data.csv')

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # eat the header
    next(csvreader)
    
    #convert the date into a list
    csvdata = list(csvreader)  
   
    # pull list first column and then len for count
    months = [row[0] for row in csvdata]
    totmonths = (len(months))  
    
    #pull list second colum and sum
    profit = [int(row[1]) for row in csvdata]
    netprofits = sum(profit)

    #iterate starting on second row to and minus from first row 
    profchange = [profit[i] - profit[i-1] for i in range(1,len(months))]
   
    #math to create average change
    avgchg = (sum(profchange)/(len(months)-1))
    
    #iterate with the difference and the month to get min max
    minmax = [(profit[i] - profit[i-1], months[i]) for i in range(1,len(months))]
    
    #math to create average change
    maxminmax = max(minmax)
    minminmax = min(minmax)

print(f"Finanical Analysis")
print(f"--------------------------------------------")
print(f"Total Months: {totmonths}")
print(f"Total: ${netprofits:,}")
print(f"Average Change: ${avgchg:,.2f}")
print(f"Greatest Increase in Profits: {maxminmax[1]} ${maxminmax[0]:,}")
print(f"Greatest Decrease in Profits: {minminmax[1]} ${minminmax[0]:,}")

# Financial Analysis
# ---------------------------- 
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)

    # profchange = []
    # for i in range(1,len(months)):
    #     profit_change = profit[i] - profit[i-1]
    #     profchange.append(profit_change)
    # pro fchangetot = sum(profchange)
    # totalchange = profchangetot/len(months)
    # print(profchangetot)
    # print(totalchange)
    # print(csvdata)

# # Read each row of data after the header
#     #csvdata = list(csvreader)
#     for row in csvreader:
#          #print(row)

# #Add the total number of months (row 0 of the csv)
# #referenced Python activity 1 module 9 
#         months_total.append(row[0])
#         profit_loss.append(int(row[1]))
#         # print(profit_loss)

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

# import os
# import csv

# csvpath = os.path.join('Resource', 'budget_data.csv')
# sum = 0
# sumchg = 0
# months=1
# with open(csvpath) as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")

# #     # Skip the header
#     next(csvreader)
# #     first_row=next(csvreader)
#     value = int(first_row[1])
#     print(value)
#     sum  =int(first_row[1])
#     print(sum)
#     # Pass the raw text data as a list
#     csvdata = list(csvreader)
#     for row in csvdata:
#         months = months + 1
#         sum = sum + int(row[1])
#         change = int(row[1]) - value
#         sumchg = sumchg + change
#         value = int(row[1]) 
    
# total_months = len(list(csvdata))+1

  
#     # SRead each row of data after the header

# print(sumchg)
# Avgchg = sumchg/total_months
# print("Financial Analysis")
# print("---------------------")
# print(f"Total Months: {total_months}")
# print(f"Total: {sum}")
# print(f"Average Change: {Avgchg}")


# with open(csvpath) as csvfile:

#     csvreader = csv.reader(csvfile, delimiter=",")

#     # Skip over the csv file header on the first row
#     next(csvreader)

#     # Pass the raw text data out as a list
#     csv_data = list(csvreader)
    
  
# for row in csv_data:
#     print(f"{row[0]:8}  {int(row[1]):14,.0f}")
#     sum = sum(row[1])
#     print(sum)
