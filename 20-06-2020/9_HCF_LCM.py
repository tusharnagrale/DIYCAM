#Write a python program to find Highest Common Factor (HCF) and Least Common Multiple (LCM) of two integers.

def LCM_HCF(num1,num2):

    #condition to check entered numbers are numeric
    if num1.isnumeric() and num2.isnumeric():

        #finding smaller number for finding its highest factor
        if num1 > num2:
            smaller = num2

        else:
            smaller = num1

        #range is till the smaller one because the smallest one could be the divisor of dividend but vice versa not possible
        #the highest value of divisor is the HCF
        for divisor in range(1,smaller + 1):

            if ((num1 % divisor == 0) and (num2 % divisor == 0)):
                HCF = divisor

        print("HCF is\n",HCF)

        LCM = (num1 * num2)// HCF

        print("LCM is", LCM)

    else:
        print("please enter numbers")

#take two numbers from user
print("Enter two numbers to find HCF and LCM: ")

num1= int(input("first number : \n"))
num2 = int(input("second number : \n"))


#calling function
LCM_HCF(num1,num2)