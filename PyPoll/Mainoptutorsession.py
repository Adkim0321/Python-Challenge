
import os
import csv

csvpath = os.path.join('PyPoll','Resource', 'election_data.csv')
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
        candidate_dict[row[2]] = [candidate_dict.get(row[2],0) + 1,(candidate_dict[row[2]] / float(total_votes))]
        # divde each cadidate's by the total votes
        #https://stackoverflow.com/questions/47893854/dictionary-math-in-python-keys-are-there-values-coming-up-empty
       
        #merge two dictionaries with the same candidates to have % and totals
   
    # for name,count in candidate_dict.items():
    print(candidate_dict)
#  print(f"{name}: {count/total_votes:0%} {count:.0f}")
    
print("Election Results")
print("------------------------------------")
print(f"total vote count: {total_votes:,}")
print("------------------------------------")
print(f"{candidate_dict}")



# The percentage of votes each candidate won: for loop new list and take the value / total len votes


# The total number of votes each candidate won loop : this is handled above


# The winner of the election based on popular vote: pick max




# As an example, your analysis should look similar to the one below:
# Election Results
# -------------------------
# Total Votes: 3521001
# -------------------------
# Khan: 63.000% (2218231)
# Correy: 20.000% (704200)
# Li: 14.000% (492940)
# O'Tooley: 3.000% (105630)
# -------------------------
# Winner: Khan





