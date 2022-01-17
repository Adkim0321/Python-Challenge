# a = ["Abhi",23,'gopal',55]

# #for,with,Cig,elif,else : 
# # Looping through every value of list
# # for i in a:

# #     print(i)


# # # Looping through just the indexes of list [ 0,1,2,3] 
# # for i in range(len(a)):
# #     print(a[i])

# for i in enumerate(a):
#     print(i)


# ## Manipulating the list
# a = ["Abhi",23,'gopal',55]
# print(a[2])

# print(a.append(5))
# print(a.remove('Abhi'))


## List of lists
a = [["Abhi",23],['gopal',55]]
b =[]
for i,value in enumerate(a):
    b.append(value[1])

bsum = sum(b)
print(b/bsum)







