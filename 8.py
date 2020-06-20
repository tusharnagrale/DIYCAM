num = input("enter the number: ")

if num.isalpha():
    print("please enter number")
elif num[::-1] == num:
    print(num,"is pallindrome")
else:
    print(num,"is not pallindrome")