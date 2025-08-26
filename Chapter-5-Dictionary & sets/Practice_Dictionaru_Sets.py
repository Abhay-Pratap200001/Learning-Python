# Q1: Create dictionary with students & marks.
student = {"Abhay":85, "Anuskha":92, "Ratankar":98}
print(student)




# Q2: Check if key exists.
student = {"Abhay":85, "Anuskha":92, "Ratankar":98}
if "Abhay" in student:
    print("Abhay is Present")
else:
    print("Not exist")




# Q3: Merge two dictionaries.
dict1 = {"a":2, "b":3}
dict2 = {"c":6, "d":8}
mergedic = {**dict1, **dict2}
print(mergedic)




# Q4: Union & Intersection of sets.
set1 = {1,2,3,4,5,6}
set2 = {0,1,2,34,7}
print("Union:", set1 | set2) 
print("Intersction", set1 & set2)




# Q5: Remove element with discard().
dic = {1,2,4,0,55,4}
dic.discard(4)
print(dic)