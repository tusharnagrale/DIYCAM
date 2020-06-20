# Write a python program to compute the frequency of characters in a string, I.e which character is present how many times in a string.
#    Consider only lower-case. Ignore upper-case and special characters.

from collections import Counter
#Counter module gives us Counter() is count the occurance of characters



def count(string):
    "count function count the lower case alphabet"

    bad_chars = [';', ':', '!', "*", " ", '(', ')', '-' , '=', '+', '#', '$', '%', '^', '&', '`', '~',
                 ',', '.', '?', '?', '/', '{', '}','@']

    #for loop for removing special characters
    for i in bad_chars :
        string = string.replace(i,'')

        #for loop for removing uppercase letters replace() is used
        for char in string:
            if char.isupper():
                string = string.replace(char,'')


    res = Counter(string)

    print ("Count of all characters in: \n",string,"is:\n"+ str(res))

#take string as input from user
string = input("enter the string: \n")

#calling function
count(string)

