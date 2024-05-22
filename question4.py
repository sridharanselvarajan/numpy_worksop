#write a program to find the sum of digits of a given number'
def sum_of_digits(n):
    sum = 0
    n = abs(n) 
    while n > 0:
        r = n % 10
        sum += r
        n //= 10  
    print(sum)

num = int(input("Enter the number: "))
sum_of_digits(num)
