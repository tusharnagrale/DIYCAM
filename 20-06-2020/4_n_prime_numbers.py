#Write a python program to print first 'n' prime numbers.


def prime_number(num):
    counter = 0

    #'number' is use to find the prime numbers it will iterate
    # untill the user gets desired number of prime numbers
    number = 1

    while True:

        #"count" : number of times the remainder is zero
        count=0;

        for n in range (1, (number+1), 1):
            remainder = number % n

            #remainder is zero is number is fully divisible by number lesser than itself
            if (remainder == 0):
                count = count+1


        #only if count is 2 then only the number is prime
        if (count==2):
            print (number)

            #"counter" : the number of prime numbers are printed
            counter = counter + 1
            if counter >= num:
                break
        number=number+1

#take input from user
num = int(input("Enter the number:"))

#take input from user
prime_number(num)