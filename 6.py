ch = input("Enter a character: ")
vowels = ['a','e','i','o','u','A','E','I','O','U']

if ch.isalpha():
    if vowels.__contains__(ch):
        print(ch, "is a vowel")
    else :
        print(ch ,"is a consonent")
else:
    print("invalid input. please enter alphabet")


