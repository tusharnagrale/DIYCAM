#Write a python program to remove spaces
#when they occur more than one time consecutively in string anywhere and print the string.
import re

def spaces_removal(string):
    "spaces_removal() replaces multiple spaces with singes space"

    #"+" sign after space indicates that the it will search for one or more than one then it will replace will single space
    res = re.sub(' +', ' ', string)
    print("The strings after extra space removal : " + str(res))


string = input("Enter the string :")

spaces_removal(string)