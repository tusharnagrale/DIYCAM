print("enter two numbers")
a = input("enter value of A: \n")
b = input("enter value of B: \n")

if a.isnumeric() and b.isnumeric():
    print("\nvalue of A is {0} and B is {1} before swapping\n".format(a,b))
    a,b = b,a

    print("value of A is {0} and B is {1} after swapping\n".format(a,b))
else:
    print("please enter numberic values")