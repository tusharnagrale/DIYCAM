#Write a python program to check if a given number is palindrome or not.

def pallindrome(num):
    'pallindrome fuction checks whether the entered number is pallindrome or not'

    #isalpha checks whether the entered input is alphabet or not
    # if the string contains alphabet then it prints "please enter number"
    if num.isalpha():
        print("please enter number")

    elif num[::-1] == num:
        print(num,"is pallindrome")

    else:
        print(num,"is not pallindrome")

#take input from user
num = input("enter the number: ")

#calling the function
pallindrome(num)