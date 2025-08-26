# Q1: Check even or odd.
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("odd")


# Q2: Check positive, negative, or zero.
num = 5
if num > 0:
    print("positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")


# Q3: Largest of three numbers.
a, b, c = 12, 15, 20

if a>b and a>c:
    print("A is largest", a)
elif b>a and b>c:
    print("b is largest", b) 
else:
    print("C Largest", c)