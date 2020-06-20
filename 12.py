def reverse (array):
    return list(reversed(array))

n = int(input("please enter the number of elements you want to enter in array: "))
lst = []
for i in range(0, n):
    ele = int(input())
    lst.append(ele)

print("original sequence of array:\n",lst)
print("array after reverse operation:\n",reverse(lst))