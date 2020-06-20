n = int(input("enter the length of array : "))
lst = []
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print("largest element in array is",max(lst),"and its location is",lst.index(max(lst)))