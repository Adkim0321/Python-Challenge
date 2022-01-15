import os
import csv

csvpath = os.path.join('Resource', 'election_data.csv')
candidate_dict = {}
total_votes = 0

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

   # Skip the header
    next(csvreader)



    for row in csvreader:
        candidate_dict[row[2]] = candidate_dict.get(row[2],0) + 1
        total_votes += 1
    print(candidate_dict)
    print(total_votes)

print(candidate_dict[row[0]])

