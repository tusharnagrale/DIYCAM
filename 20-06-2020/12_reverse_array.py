#Write a python program to reverse elements of an array.

def reverse(array):
    "reversed() is used to reverse the content of array"
    return list(reversed(array))

length = int(input("please enter the length of array: "))

array = []
for i in range(0, length):
    ele = int(input("enter the element at position {0} :".format(i)))
    array.append(ele)

print("original sequence of array:\n",array)

print("array after reverse operation:\n",reverse(array))