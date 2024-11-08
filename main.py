#PYTHON PRACTICE QUESTIONS
#Conditional statements
#Question no 1
#traffic light code
light=input("enter light color: ")
if (light=="red"):
    print("please stop ")
elif (light=="green"):
    print("go")
elif (light=="yellow"):
    print("please look around")
else:
    print("light is broken")
#---------------------------------------------------------------------------------
#Question no 2
#student grades
marks =int (input("enter your marks: "))
if(marks >= 90 and marks < 100) :
    print("grade A")
elif (marks >= 80 and marks < 90):
    print ("grade B")
elif (marks >= 70 and marks < 80):
    print("grade C")
else:
    print("fail")
#-----------------------------------------------------------------------------------
#question no 3
#print output for: (A=5, G=M) , (A=2 , G=F)
A = int(input("A= "))
G = input(" M/F= ")
if ((A==1 or A==2) and G=="M"):
    print("fee is 100")
elif ((A==3 or A==4) and G=="f"):
    print("fee is 200")
elif ( A==5 and G=="f"):
    print("fee is 300")
else:
    print("no fee")
#------------------------------------------------------------------------------------
#ternary operator or single line if
   #Question no 4
#<var>= <val1> if <condition> else <val2>
food= input("food: ")
eat = "yes" if food== "cake" else "no"
print(eat)
#------------------------------------------------------------------------------------
  #Question no 5
#<stt1> if <condition> else <stt2>
food =input("food: ")
print("sweet") if food=="cake" or food=="jalebi" else print ("not sweet")
#------------------------------------------------------------------------------------
#question no 6
#write a program to input two numbers and print their sum
num1=int(input("enter your 1st number: "))
num2=int(input("enter your 2nd number: "))
num3=num1+num2
print(num3)
#--------------------------------------------------------------------------------------
#question no 7
# write a program to input side of a square and print its area
side=int(input("enter the side of square"))
square= side*side
print(square)
#--------------------------------------------------------------------------------------
#question no 8
# write a program to input two floating numbers and print their average.
num1=float(input("enter your first number= "))
num2=float(input("enter your second number= "))
num3=(num1+num2)/2
print(num3)
#-----------------------------------------------------------------------------------------
#question no 9
#write a program to input two int numbers, a and b.print true if a is grater than or equal to b.if not print false.
num1=int(input("enter first number: "))
num2=int(input("enter second number: "))
if num1>=num2:
    print(True)
else:
    print(False)
#------------------------------------------------------------------------------------------
#question no 10
# write a program to input users first name and print its length
name=str(input("enter your first name: "))
print(len(name))
#--------------------------------------------------------------------------------------------
#question no 11
# write a program to find the occurance of $ in a string
str="hi, i am the $ symbol $99.99"
print(str.count("$"))
# -----------------------------------------------------------------------------------------------
# question no 12
# write a program to get license for vote
age=int(input("enter your age: "))
if(age>=18):
    print("you can vote")
else:
    print("you cannot vote")
#--------------------------------------------------------------------------------------------------
#question no 13
#traffic license
age=int(input("enter your age: "))
if(age>=18):
    if(age>=80):
        print("you cannot drive")
    else:
        print("you can drive")
else:
    print("you cannot drive")
#----------------------------------------------------------------------------------------------------
# question no 14
# write a program to check if a number entered by the user is odd or even
num=int(input("enter a number here: "))
if(num%2==0):
    print("number is even")
else:
    print("number is odd")
# --------------------------------------------------------------------------
# question no 15
# write a program to find the greatest of three numbers entered by the user
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))
if(a>=b and a>=c):
    print("first number is greater")
elif(b>=a and b>=c):
    print("second number is greater")
else:
    print("third number is greater")
# --------------------------------------------------------------------------
# question no 16
# write a program to check if a number is a multple of 7 or not
num=int(input("enter a number: "))
if(num%7==0):
    print("number is a multiple of 7")
else:
    print("number is not a multiple f 7")
# ----------------------------------------------------------------------------
# question no 17
# write a program to ask the user to enter names of their three favourite movies and store them in a list
movie1=str(input("enter the name of your first favourite movie: "))
movie2=str(input("enter the name of your second favourite movie: "))
movie3=str(input("enter the name of your third favourite movie: "))
list=[]
list.append(movie1)
list.append(movie2)
list.append(movie3)
print(list)
# ------------------------------------------------------------------------------
# question no 18
# WAP to check if a list contains a palindrome of elements. [hint:use copy()method]
list1=[1,2,1]
copy_list=list1.copy()
copy_list.reverse()
if(copy_list==list1):
    print("palindrome")
else:
    print("not a palindrome")
# -------------------------------------------------------------------------------
# question no 19
# WAP to count the number of students with grade "A" in the following tuple
grades=("C","A","A","B","D")
print(grades.count("A"))
# --------------------------------------------------------------------------
# qestion no 20
# stores the values in a list and sort them from "A" to "D"
values=str('A','C','B','C','D')
values.sort()
print(values)
# ---------------------------------------------------------------------------------

