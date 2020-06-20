#Write a python program to check if the number is odd or even using conditional operator.

def even_odd(num):
   "function to find whether the number is even or odd"
   if (num % 2) == 0:
      print("{0} is Even".format(num))

   else:
      print("{0} is Odd".format(num))

#take input from user
num = int(input("Please enter a number: "))