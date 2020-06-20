num = (input("enter the no"))

if num.isnumeric():
    sum = 0
    for n in str(num):
        sum = sum + int(n)
    print("sum of digits is",sum )
else :
    print("invalid input")
