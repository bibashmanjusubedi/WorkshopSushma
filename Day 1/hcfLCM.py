a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
 
HCF = 1
 
for i in range(2,a+1): # for loop
    if(a%i==0 and b%i==0):
        HCF = i

LCM = (a*b)//HCF # integer divison
 
print("First Number is: ",a)
print("Second Number is: ",b)
print("HCF of the numbers is: ",HCF)
print("LCM of the numbers is:", LCM)