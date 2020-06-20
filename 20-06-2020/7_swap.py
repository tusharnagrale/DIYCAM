#Write a python program to swap two numbers without using temp or temporary or third variable.

def swap(num1,num2):
    "swap function swaps the values of two varaibles"

    #to check whether the entered numbers are numeric or not
    if num1.isnumeric() and num2.isnumeric():
        print("\nvalue of num1 is {0} and num2 is {1} before swapping\n".format(num1,num2))
        num1,num2 = num2,num1

        print("value of num1 is {0} and num2 is {1} after swapping\n".format(num1,num2))
    else:
        print("please enter numberic values")


print("enter two numbers")

#take two numbers
num1 = input("enter value of num1: \n")
num2 = input("enter value of num2: \n")

#calling swap function
swap(num1,num2)