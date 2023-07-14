#program to check positive Negative And Zero

n=int(input("Enter the Number"))
if n >0:
    print(n," is Positivi")
elif n < 0:
    print(n," is Negative")
else:
    print(n," is equals to Zero")

#program to check largest number
a=int(input("Enter the first Number"))
b=int(input("Enter the second Number"))
c=int(input("Enter the third Number"))

if a<b:
    if b<c:
        print(c," is greater")
    else:
        print(b," is greater")
elif a<c:
    print(c," is greater")
else:
    print(a," is greater")

#program to find leap year

year=int(input("Enter the Year"))
if (year % 100 != 0):
    if (year % 4 == 0):
        print(year," is leap year")
    else:
        print(year," is not a leap year")
else:
    print(year," is not a leap year")
    
#program to check the strings anagram are not

s1=str(input("enetr the first string"))
s2=str(input("enetr the second string"))
if sorted(s1)==sorted(s2):
    print("strings are anagram")
else:
    print("string are not anagram")
    
#program to give Grade
def grade():
    grade=input("Enter the Grade:")
    print(grade)
    if grade=='A':
        print("Excellent")
    elif grade=='B':
        print("Very Good")
    elif grade=='C':
        print("Good")
    elif grade=='D':
        print("ok")
    elif grade=='F': 
        print("Fail")     
    else:
        print("No Grades Like This")        
grade()

#prodram to find product is positivi negative or zero

num1=int(input("Enter the number1:"))
num2=int(input("Enter the number2:"))
print("Product is:",num1*num2)

if (num1*num2)>0:
    print("Product is +ve")
    
elif (num1*num2)<0:
        print("Product is -ve")
    
else:
    print("Product is -Zero")



#program to find even or odd
num=int(input("Enter the Number:"))
print("Number",num)

if num%2==0:
    print(num," is even")
else:
    print(num, " is odd")
    
#program find string or digit
a=input("Enter the Character:")
if a.isdigit():
    print(a," is digit")
else:
    print(a,"is alpabet")

#program find prime or not
num = int(input("Enter a number: "))

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")
else:
   print(num,"is not a prime number")



