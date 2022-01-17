
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
        # divde each cadidate's by the total votes
        #https://stackoverflow.com/questions/47893854/dictionary-math-in-python-keys-are-there-values-coming-up-empty
        candidate_perc[row[2]] = (candidate_dict[row[2]] / float(total_votes))
        #merge two dictionaries with the same candidates to have % and totals
    #https://favtutor.com/blogs/merge-dictionaries-python#:~:text=We%20can%20combine%20two%20dictionaries%20in%20python%20using%20dictionary%20comprehension.&text=If%20both%20the%20dictionaries%20have,example%20for%20a%20better%20understanding.
    def mergeDictionary(candidate_dict, candidate_perc):
        summ_candidate = {**candidate_dict, **candidate_perc}
        for key, value in summ_candidate.items():
            if key in candidate_dict and key in candidate_perc:
               summ_candidate[key] = [value , candidate_dict[key]]
        return summ_candidate
    summ_candidates = mergeDictionary(candidate_dict, candidate_perc)
    print(summ_candidates)
    #print out the new percent values with the respective candidates
    valuesperc = candidate_dict.values()
    #pick winner through max values 
    max_values = max(candidate_dict, key=candidate_dict.get)

# for name,count in candidate_dict.items():
#     print(f"{name}: {count/total_votes:0%} {count:.0f}")
    
print("Election Results")
print("------------------------------------")
print(f"total vote count: {total_votes:,}")
print("------------------------------------")
print(f"{candidate_dict}")
# print(candidate_perc)
# print(summ_candidates)
   #https://stackoverflow.com/questions/17330139/python-printing-a-dictionary-as-a-horizontal-table-with-headers
print("{:<8} {:^8} {:^8}".format('Candidate','%','Total Votes'))
for key, value in summ_candidates.items():
    label, num = value
    print("{:<8} {:^10,.0%} {:>10,.0f}".format(key, label, num))
print("------------------------------------")
print(f"winner: {max_values}")
print("------------------------------------")


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