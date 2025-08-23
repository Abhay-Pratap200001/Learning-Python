# age = int(input("Enter the age: "))

# if(age >= 18):
#     print("Yes")
# else:
#     print("No")


# u1 = int(input("Enter num 1: "))
# u2 = int(input("Enter num 2: "))
# u3 = int(input("Enter num 3: "))
# u4 = int(input("Enter num 4: "))

# if(u1>u2 and u1>u3 and u1>u4):
#     print("U1 is greater")

# elif(u2>u1 and u2>u3 and u2>u4):
#     print("U2 is greater")

# elif(u3>u1 and u3>u2 and u3>u4):
#      print("U3 is gretaer num")
    
# else:
#     print("U4 is greater")


marks1 = int(input("Enter num 1: "))
marks2 = int(input("Enter num 2: "))
marks3 = int(input("Enter num 3: "))

totlper = (marks1 + marks2 + marks3)/300 * 100


if(totlper >= 40):
    print("pass")

elif(totlper >= 60):
    print("Pass with second position")

else:
    print('FAILED')