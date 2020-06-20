import re

def spaces_removal(string):
    res = re.sub(' +', ' ', string)
    print("The strings after extra space removal : " + str(res))


string = input("Enter the string :")
spaces_removal(string)