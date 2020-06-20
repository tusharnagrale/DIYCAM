#Write a python program to print any multiplication table up to 10.
def table(num):
    for i in range(1,11):
       print(num,'x',i,'=',num*i)

num = int(input("Enter the number: "))

table(num)