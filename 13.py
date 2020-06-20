from collections import Counter

string = input("enter the string: \n")

bad_chars = [';', ':', '!', "*", " ", '(', ')', '-' , '=', '+' ]
#for loop for removing special characters
for i in bad_chars :
    test_string = string.replace(i, '')

res = Counter(string)

print ("Count of all characters in: \n",string,"is:\n"+ str(res))