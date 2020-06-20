#Write a python program to add the digits of a number.


def add_digits_of_number(number):

    #is.numeric() returns True if the string is numeric, if the string is not
    #numeric then it will give output "invalid input"
    if number.isnumeric():
        sum = 0


        #number is converted into string so that the num should be iterated
        for num in str(number):
            sum = sum + int(num)

        print("sum of digits is",sum )
    else :
        print("invalid input")

#input function to take input from user
number = (input("enter the number: "))

#calling function with number as a parameter
add_digits_of_number(number)