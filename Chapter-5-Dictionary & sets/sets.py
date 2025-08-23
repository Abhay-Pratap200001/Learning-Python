# In Python, a set is an unordered collection of unique and immutable elements. Sets are defined using curly braces {} or the set() constructo
s = {1,2,3,4,5,6}

s.add(20)

# # use to add more values but can add dublicate
print(s, type(s))
s.remove(5)
print(s)


ans=s.clear()
print(ans)



s.__len__()
print(s)

# take both of values and do not repeated
s1 = {1,45,6}
s2 = {7,8,1,78}
print(s1.union(s2))

# in intersection take from both of common values
print(s1.intersection(s2))


print({1,45,6}.issubset(s1))
print({1,45,6}.issuperset(s1))


