#Write a python program to find maximum or largest element present in an array and
#prints the location or index at which maximum element occurs in array.

def largest_element(length):
    "function to find largest element in an array"
    list = []

    for i in range(1, length+1):
        ele = int(input("enter the element no {0} :".format(i) ))
        list.append(ele)

    #max() finds the maximum or largest element from list and index() return the location of element
    print("largest element in array is",max(list),"and its location is",(list.index(max(list))))

#take length of array
length = int(input("enter the length of array : "))

largest_element(length)