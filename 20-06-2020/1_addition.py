#Write apython program to accept two numbers from users for addition
#  & ask user if he wants to repeat the addition with other numbers.

while True:

    print("enter the two no. for addition\n")

    #to take input from user
    num1 = int(input("enter the first no: \n"))
    num2 = int(input("enter the second no: \n"))

    print("sum is",num1 + num2)

    #to take choice from the user whether he/she wants to repeat addition
    choice = input("do you want to continue the addition with other numbers? Y/N: ")
    choice = choice.upper()



    #1) if user gives input "Y" then it will allow user to perform operation again.
    #2) if user gives input "N then it will break the loop and program will be terminated.
    #3) if user gives input other than Y/N then it gives "invalid option!! you can continue addition".

    if choice == "Y":
        pass
    elif choice == "N":
        break
    else:
        print("invalid option!! you can continue addition\n")





