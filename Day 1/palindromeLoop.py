#Enter input string 
string = input("Enter string : ") 
 
#Declare an empty string variable   
revstr = "" 
 
#Iterate string with for loop 
for i in string:
    revstr = i + revstr 
print("Reversed string : ", revstr) 
 
if(string == revstr): 
    print("The string is a palindrome.") 
else: 
    print("The string is not a palindrome.")