# Arithmetic Operators
# Used for basic math.
a = 10
b = 3
print(a + b)   # 13 (Addition)
print(a - b)   # 7  (Subtraction)
print(a * b)   # 30 (Multiplication)
print(a / b)   # 3.333... (Division)
print(a % b)   # 1  (Modulus / remainder)
print(a ** b)  # 1000 (Exponentiation -> 10^3)
print(a // b)  # 3  (Floor division)



# Comparison Operators
# Used to compare values (result is True/False).
x = 5
y = 10
print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= y)  # False
print(x <= y)  # True



# Logical Operators
# Used for combining conditions.
p = True
q = False
print(p and q)  # False (both must be True)
print(p or q)   # True  (any one True)
print(not p)    # False (opposite of True)




# Assignment Operators
# Used to assign values.
x = 10
x += 5   # x = x + 5
print(x)  # 15



# Membership Operators
# Check if value exists in a sequence.
nums = [1, 2, 3, 4]
print(2 in nums)     # True
print(5 not in nums) # True



# Identity Operators
# Check if two objects share the same memory location.
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(x is y)      # True  (same object)
print(x is z)      # False (different objects with same values)
print(x is not z)  # True


