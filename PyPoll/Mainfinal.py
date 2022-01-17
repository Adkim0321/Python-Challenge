
import os
import csv

csvpath = os.path.join('Resource', 'election_data.csv')
candidate_dict = {}
candidate_perc = {}
total_votes = 0

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

   # Skip the header
    next(csvreader)

    for row in csvreader:
        #get totals
        total_votes += 1
        # go through the list and find the inference of the candidates and tally total
        candidate_dict[row[2]] = candidate_dict.get(row[2],0) + 1
    valuesperc = candidate_dict.values()
    #pick winner through max values 
    max_values = max(candidate_dict, key=candidate_dict.get)
    

    
print("Election Results")
print("------------------------------------")
print(f"total vote count: {total_votes:,}")
print("------------------------------------")
#print(f"{candidate_dict}")
#print(candidate_perc)
print("{:<8} {:^8} {:^8}".format('Candidate','%','Total Votes'))
for name,count in candidate_dict.items():
    print(f"{name:<8}: {count/total_votes:^8.0%} {count:^8,.0f}")
print("------------------------------------")
print(f"winner: {max_values}")
print("------------------------------------")

# https://stackoverflow.com/questions/48959098/how-to-create-a-new-text-file-using-python/48964410
# When writing a .txt file, use "x" if the file doesn't exist and use "w" if file exists and needs to be written/changed/appended
# https://www.freecodecamp.org/news/python-new-line-and-how-to-python-print-without-a-newline/#:~:text=The%20new%20line%20character%20in%20Python%20is%20%5Cn%20.,used%20to%20separate%20the%20lines
# Use "\n" in the f.write string to move text to next line for better file viewing
#start with this to create
#with open("Analysis/PyPoll_Analysis.txt", "x") as f:
#use this to edit
with open("Analysis/PyPoll_Analysis.txt", "w") as f:
    f.write("Election Results\n")
    f.write("------------------------------------\n")
    f.write(f"total vote count: {total_votes:,}\n")
    f.write("------------------------------------\n")
    f.write("{:<8} {:^8} {:^8}".format('Candidate','%','Total Votes\n'))
    for name,count in candidate_dict.items():
        f.write(f"{name:<8}: {count/total_votes:^8.0%} {count:^8,.0f}\n")
    f.write("------------------------------------\n")
    f.write(f"winner: {max_values}\n")
    f.write("------------------------------------")
