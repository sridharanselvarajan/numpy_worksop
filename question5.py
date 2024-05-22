#write a program to find if the given number is prime no or not

def prime(n):
    if n <= 1:
        print("It is not a prime number")
        return

    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1

    if count == 0:
        print("It is a prime number")
    else:
        print("It is not a prime number")

n = int(input("Enter the number: "))
prime(n)
