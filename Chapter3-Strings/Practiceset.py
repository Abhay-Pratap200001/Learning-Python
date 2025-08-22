name = input("Enter you name :")
print(f"My Name is {name}")


letter = ''' Hello <|Name|>,
           you are selected on!
           <|Date|>'''

print(letter.replace("<|Name|>", "Abhay").replace("<|Date|>", "20 December"))


name = "Abhay you are  selected"
print(name.find("  "))

name = "Abhay you are  selected"
print(name.replace("  ", " "))


