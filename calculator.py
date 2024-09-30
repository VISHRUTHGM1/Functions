def div(a,b):
    print(f"division of {a} and {b} is {a/b}")
def add(a,b):
    print(f"addition of {a} and {b} is {a+b}")
def sub(a,b):
    print(f"subtraction of {a} and {b} is {a-b}")
def mul(a,b):
    print(f"multiplication of {a} and {b} is {a*b}")
def mod(a,b):
    print(f"modulus of {a} and {b} is {a%b}")
one = float(input("Enter first number:"))
two = float(input("Enter second number:"))
ans = input("Enter operation to be performed:")
if ans == "add":
    add(one,two)
elif ans == "divide":
    div(one,two)
elif ans == "modulus":
    mod(one,two)
elif ans == "subtract":
    sub(one,two)
elif ans == "multiply":
    mul(one,two)
else:
    print("You entered the wrong input!")