import os
import csv

csvpath = os.path.join('Resource', 'election_data.csv')

with open(csvpath, encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

   # Skip the header
    next(csvreader)
    csvdata= list(csvreader)

#data is headered as voteid county candidate
# The total number of votes cast, grab fist column and len column
    votes = [row[0] for row in csvdata]
    totalvotes = (len(votes))  
    print(totalvotes)
    # vote = []
    # for row in csvdata:
    #     votes = row[0]
    #     vote.append(row[0])
    # print(len(vote))
# A complete list of candidates who received votes: loop candiates and summate total:put in list
    candidates = [row[2] for row in csvdata]
    # i need the name of the candidates and the respective total vote count of the candidates
    #candidate 1 votes x
    #candidate 2 votes y
    
    dict_candidates = {}

    for i in candidates:
        dict_candidates[i] = dict_candidates.get(i,0) + 1

    print(dict_candidates)




# Python program to count the frequency of
# elements in a list using a dictionary

# import os
# import csv

# csvpath = os.path.join('Resource', 'election_data.csv')

# with open(csvpath, encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile, delimiter=",")

#    # Skip the header
#     next(csvreader)
#     csvdata= list(csvreader) 
#     candidates = [row[2]for row in csvdata]
#     def CountFrequency(my_list):
    
#     # Creating an empty dictionary
#         freq = {}
#         for items in my_list:
#             freq[items] = my_list.count(items)
     
#         for key, value in freq.items():
#             print ("% d : % d"%(key, value))
 
# # Driver function
#     if __name__ == "__main__":
#         my_list = candidates
#         CountFrequency(my_list)
  

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
# -------------------------


