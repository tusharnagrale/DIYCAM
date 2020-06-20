#Write a python program to find factorial of a given number using for loop.

#function to fnd factorial
def factorial(num):
    fac = 1
    for i in range(1, num + 1):
        fac = fac * i

    print("factorial of ", num, " is ", fac)


#to take input from user
num = int(input("enter a number: "))
fac = 1

#calling function
factorial(num)