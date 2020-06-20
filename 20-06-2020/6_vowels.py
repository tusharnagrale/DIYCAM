#Write a python program to checks whether an input alphabet is a vowel or not.
# Both lower-case and upper-case are checked.


def find_vowels(char):

    #isalpha checks whether the character is alphabets or not and returns 'True' and 'False'.
    #if input is other than alphabet then it will print "number or special charater inserted. please enter alphabet"
    if char.isalpha():

        #to check the input length should be only one
        if len(char) == 1:

            #contains checks char with every element in vowels
            if vowels.__contains__(char):
                print(char, "is a vowel")
            else :
                print(char ,"is a consonent")

        else:
            print("please enter single character")

    else:
        print("number or special charater inserted. please enter alphabet")

#to take character from user
char = input("Enter a character: ")

#list of vowels to check with input
vowels = ['a','e','i','o','u','A','E','I','O','U']

find_vowels(char)