#write a program to find the maximum of two numbers
def find_maximum(a, b):
    if a > b:
        return a
    else:
        return b
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
maximum = find_maximum(num1, num2)
print("The maximum of the two numbers is:", maximum)
