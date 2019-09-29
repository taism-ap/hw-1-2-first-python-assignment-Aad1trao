def subtract(x,y):
    return x-y
def add(x,y):
    return x+y
def multiply(x,y):
    return x*y
def divide (x,y):
    return x/y

num1 = int(input("Choose a number:"))
num2 = int(input("Choose another number:"))
choice = input("Choose either: +, -, /, *.")

if choice == '+':
    print(num1, "+", num2, "=", add(num1,num2))

if choice == '-':
    print(num1, "-", num2, "=", subtract(num1,num2))

if choice == '*':
    print(num1, "*", num2, "=", multiply(num1,num2))

if choice == '/':
    print(num1, "/", num2, "=", divide(num1,num2))

