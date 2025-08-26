# Q1: Count how many times the letter 'a' appears in a string.
text= "banana apple mango"
count_a = text.count("a")
print(count_a)



# Q2: Reverse a string without slicing ([::-1]).
text = "Hello World"

reversed_text = ""

for char in text:
    reversed_text = char + reversed_text
    print("Reversed str:", reversed_text)




# Q3: Check if a string is a palindrome.
world = "MaM"
if world == world[::-1]:
    print("Palindrome")
else:
    print("Not Palindrom")



# Q4: Convert string to title case.
text = "PYTHON PROGRAMMING IS FUN"
print(text.title())




# Q5: Replace all spaces with '-'.
text = 'Pyhon   is   easy'
new_text = text.replace("   "," ")
print(new_text)