print("Enter two numbers to find HCF and LCM: ")
n1= int(input("first number : \n"))
n2 = int(input("second number : \n"))
if n1 > n2:
    smaller = n2
    larger = n1
else:
    smaller = n1
    larger = n2

for i in range(1,smaller + 1):
    if ((n1 % i == 0) and (n2 % i == 0)):
        HCF = i
print("HCF is\n",HCF)

LCM = (n1 * n2)// HCF
print("LCM is", LCM)