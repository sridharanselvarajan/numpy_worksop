#write a program to find the factorial of a nummber

def factorial_recursive(n):
    if n < 0:
        print("factorial of a number is not possible")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

n=int(input("Enter the number"))
print(factorial_recursive(n)) 
