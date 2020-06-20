while True:
    print("enter the two no. for addition\n")

    a = int(input("enter the first no: \n"))

    b = int(input("enter the second no: \n"))

    print("sum is",a + b)


    choice = input("do you want to continue the addition with other numbers? Y/N: ")
    choice = choice.upper()
    if choice == "Y":
        pass
    elif choice == "N":
        break
    else:
        print("invalid option!! you can continue addition\n")





