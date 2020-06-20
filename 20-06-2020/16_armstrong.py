#Write a python program to check if the given number is armstrong number or not.
#    A number is armstrong if the sum of cubes of individual digits of a number is equal to the number itself.
#    Ex: 0, 1, 153, 371, 407.
#    Ex: 371 is an armstrong number as 33 + 73 + 13 = 371.
def armstrong(num):
    "armstrong() : calculates the sum of the cube of each digit"

    sum = 0

    #for checking the operated and input number are same or not
    temp = num

    while temp > 0:

        #digit : remainder
        digit = temp % 10

        #sum of cubes of digits
        sum += digit ** 3

        #dividend for next loop
        temp //= 10

    if num == sum:
       print(num,"is an Armstrong number")
    else:
       print(num,"is not an Armstrong number")

#to take input from user
num = int(input("Enter a number: "))

#calling function
armstrong(num)