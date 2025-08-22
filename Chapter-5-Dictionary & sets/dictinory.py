# In Python, a dictionary is a built-in data type used to store collections of data in key:value pairs. They are also known as associative arrays or hash maps in other programming languages

marks={
    'Abhay':70,
    'Anushka':80,
    'Ratnakar':90
}
# printing all marks with name 
print(marks) 
# printing Abhay marks only
print(marks["Abhay"])


# Methods of dictionary

marks={
     'Abhay':70,
     'Anushka':80,
     'Ratnakar':90
}

#   gives key value pairs list 
print(marks.items())

# give keys of dictionary
print(marks.keys()) 

#  give values of dictionary
print(marks.values()) 

 

marks={
     'Abhay':70,
     'Anushka':80,
     'Ratnakar':90
}

marks.update({'Abhay':99})
#  updateing the value
print(marks)
# If there is no abhay key and still we use abhay to access the value of abahy we get error in noraml if we use get we dont get error we get none
print(marks.get("Abhay"))
print(marks["Abhay"])


ans = marks.pop('Abhay','Anushka')
print(ans)

# rempove the key
print(marks) 


ans = marks.popitem()
print(ans)

print(marks)