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
# question no 21
# store following word meanings in dic(cat: a small animal, table: (a piece of furniture , list of facts and figures))
dictionary= {
     "cat": " a small animal",
    "table ": ["a piece of furniture" , "list of facts and figures"]
}
print(dictionary)
# ----------------------------------------------------------------------------------------------
# question no 22
# you are given a list of subjects for students.assume 1 classroom is required for 1 subject.how many classrooms are needed by all students.python,java,c++,python,typescript,java,python,java,c++,c.
subjects={
    "python","java","c++","python","typescript","java","python","java","c++","c"
}
print(len(subjects))
print("five classroom are required for these students")
# ----------------------------------------------------------------------------------------------
# question no 23
# write a program to enter marks of 3 subjects from the user and store them in a dictionary.start with an empty dictionary and store them one by one.use subject name as key and marks are value.
marks={}
marks1=int(input("enter the marks of phy: "))
marks.update ({"phy":marks1})
marks2=int(input("enter the marks of 2 chem: "))
marks.update({"chem":marks2})
marks3=int(input("enter the marks of 3 com: "))
marks.update({"com":marks3})
print(marks)
# ----------------------------------------------------------------------------------------------
# question no 24
# figure out a way to store 9 and 9.0 as separate values in a set
numbers ={
    ("float" ,9.0),
    ("int",9)
}
print(numbers)
# ----------------------------------------------------------------------------------------------
# question no 25
# print numbers from 1 to 100
i=1
while i<=100:
    print(i)
    i+=1
#-----------------------------------------------------------------------------------------------
# question no 26
# print numbers from 100 to 1
i=100
while i>=1:
    print(i)
    i-=1
# ----------------------------------------------------------------------------------------------
# question no 27
# print multiplication table of a number n
n=int(input("enter a number: "))
i=1
while i<=10:
    print(n*i)
    i+=1
# -------------------------------------------------------------------------------------------------
# question no 28
#print the elements of a following list using a while loop [1,4,9,12,34,56,78,90,64,43,36]
nums=[1,4,9,12,34,56,78,90,64,43,36]
index = 0
while index< len(nums):
    print(nums[index])
    index+=1
#---------------------------------------------------------------------------------------------------
# question no 29
# search for a number x in this tuple using loop (1,4,9,12,34,56,78,90,64,43,36)
nums=(1,4,9,12,34,56,78,90,64,43,36)
x=int(input("enter a number from the tuple(1,4,9,12,34,56,78,90,64,43,36):  "))
i=0
while i<len(nums):
    if (nums[i]==x):
        print("found at index ",i)
    i+=1
#-----------------------------------------------------------------------------------------------------
# question no 30
# print the elements of the following list using the  for loop [1,4,9,12,34,56,78,90,64,43,36]
nums=[1,4,9,12,34,56,78,90,64,43,36]
for el in nums:
    print(el)
# -----------------------------------------------------------------------------------------------------
# question no 31
# search for a number x in this tuple using for loop (1,4,9,12,34,56,78,90,64,43,36)
nums=(1,4,9,12,34,56,78,90,64,43,36)
x=int(input("enter a number from the tuple(1,4,9,12,34,56,78,90,64,43,36):  "))
index=0
for el in nums:
    if(el==x):
        print("found at index",index)
    index+=1
# ------------------------------------------------------------------------------------------------------
# question no 32
# print numbers from 1 to 100 using range and for
for i in range(1,101):
    print(i)
# -----------------------------------------------------------------------------------------------------
# question no 33
# print numbers from 100 to 1 using range and for
for i in range(100,0,-1):
    print(i)
# -----------------------------------------------------------------------------------------------------
# question no 34
# printthe multiplication table of a number n using for and range
n=int(input("enter a number: "))
for i in range(1,11):
    print(n*i)
#----------------------------------------------------------------------------------------------------
# question no 35
# WAP to find the sum of the first n natural numbers using while loop
n=int(input("enter a natural number: "))
sum=0
i=1
while i <=n:
    sum+=i
    i+=1
print(sum)
#------------------------------------------------------------------------------------------------------
# question no 36
# WAP to find the sum of the first n natural numbers using for loop
n=int(input("enter a natural number: "))
i=1
sum=0
for i in range(1,n+1):
    sum+=i
print(sum)
#-------------------------------------------------------------------------------------------------------
# question no 37
# WAP to find the factorial of n numbers using for loop
n=int(input("enter a natural number: "))
i=1
fact=1
for i in range(1,n+1):
    fact*=i
print(fact)
# ----------------------------------------------------------------------------------------------------------
# question no 38
# WAP to find the factorial of n numbers using while loop
n=int(input("enter a natural number: "))
i=1
fact=1
while i <=n:
    fact*=i
    i+=1
print(fact)
# --------------------------------------------------------------------------------------------------------
# question no 39
# calculating average of three numbers using function
def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg
calc_avg(2,3,4)
#-----------------------------------------------------------------------------------------------------------
# question no 40
# WAP to print the length of a list (using list as a parameter)
cities=['islamabad','faisalabad','lahore']
foods=['icecream','chocolate']
def print_len(list):
    print(len(list))
print_len(cities)
print_len(foods)
# ----------------------------------------------------------------------------------------------------------------
# question no 41
# WAP to print the elements of a list in a single line (list is the parameter)
cities=['islamabad','faisalabad','lahore']
foods=['icecream','chocolate']
def print_el(list):
    for items in list:
        print(items,end=" ")
print_el(cities)
print_el(foods)
# ---------------------------------------------------------------------------------------------------------------
# question no 42
# WAP to find the factorial of n. (n is the parameter)
n=int(input("enter a number: "))
def fac(n):
    fact=1
    for i in range(1,n+1):
        fact *= i 
    print(fact)
fac(n)     
# ---------------------------------------------------------------------------------------------------------------
# question no 43
# WAP to convert US dollar into PKR
usd_val=int(input("enter usd value: "))
def converter(usd_val):
    pkr_val = usd_val*300
    print(usd_val,"USD=",pkr_val,"PKR")
converter(usd_val)
# ---------------------------------------------------------------------------------------------------------------
# question no 44
# a function takes a number as input and print odd if the number is odd and even if the number is even
n=int(input("enter a number: "))
def val_ue(n):
    if (n%2 !=0):
        print("ODD")
    else: 
        print("EVEN")
val_ue(n)
# -----------------------------------------------------------------------------------------------------------------
# question no 45
# factorial of n using recursion
n=int(input("enter a number: "))
def fac(n):
    if (n==0 or n==1):
        return 1
    return fac(n-1)* n
print(fac(n))
# -------------------------------------------------------------------------------------------------------------------
# question no 46
# write a recursive function to calculate the sum of first n natural numbers
n=int(input("enter a natural num:  "))
def calc_sum(n):
    if (n==0):
        return 0
    return calc_sum(n-1) + n
print(calc_sum(n))
# --------------------------------------------------------------------------------------------------------------------
# question no 47
# write a recursive function to print all the elements in a list.[hint: use list and index as parameters]
def print_list(list,idx=0):
    if idx == len(list):
        return
    print(list[idx])
    print_list(list, idx+1)
cities=['islamabad','lahore','faisalabad']
print_list(cities)
# ------------------------------------------------------------------------------------------------------------------
# question no 48
# create a new file practice.txt using the Python. Add the following data in it:
#       hi everyone. we are learning file I/O using python. i like programming in python.
with open("practice.txt","w") as f:
    f.write("hi everyone.\nwe are learning file I/O\n")
    f.write("using java.\nI like programming in java.")
# --------------------------------------------------------------------------------------------------------------------
# question no 49
# WAF that replaces all the occurrences of java with python in above file
with open("practice.txt","r") as f:
    data = f.read()
    updated_data = data.replace("java","python")
    print(updated_data)
    with open("practice.txt","w") as f:
        f.write(updated_data)
# --------------------------------------------------------------------------------------------------------------------
# question no 50
# search if the word learning exist in the file or not.
def find_word():
    with open("practice.txt","r") as f:
        data =f.read()
    if (data.find("learning")==-1):
        print("The word 'learning' is not found in the file.")
    else:
        print("The word 'learning' is found in the file.")
find_word()
# ----------------------------------------------------------------------------------------------------------------------
# question no 51
# WAF to find in which line of the file does the word learning occurs first.print -1 if the word is not found.

def find_line():
    word ="learning"
    data = True
    line_num = 1
    with open("practice.txt", "r") as f:
        while data:
            data = f.readline()
            if word in data:
                print(line_num)
                return
            line_num += 1
    return -1
print(find_line())
# ----------------------------------------------------------------------------------------------------------------------
# question no 52
# from a file containing numbers separated by comma, print the count of even numbers
count=0
with open ("p.txt", "r") as f:
    data = f.read()
    print(data)
    nums= data.split(",")
    for val in nums:
        if (int(val)%2==0):
            count+=1 
print(count)
# ----------------------------------------------------------------------------------------------------------------------
# question no 53
# create a student class that takes names and marks of 3 subjects as arguments in constructor.then create a method to print the average
class Student:
    def __init__(self,name,marks1,marks2,marks3):
        self.name=name
        self.marks1=marks1
        self.marks2=marks2
        self.marks3=marks3
    def calculate_avg(self):
        avg=(self.marks1+self.marks2+self.marks3)/3
        print("your average score is",avg)

student1=Student("John",85,92,88)
student1.calculate_avg()
# ----------------------------------------------------------------------------------------------------------------------
# question no 54
# create account class with 2 attributes- balance and account no.create methods for debit, credit and printing the balance.
class Account:
    def __init__(self,bal,acc_no):
        self.balance=bal
        self.account_no=acc_no
    def debit(self,amount):
        self.balance -= amount
        print("Amount debited successfully")
    def credit(self,amount):
        self.balance += amount
        print("Amount credited successfully")
    def print_balance(self):
        print("Your current balance is",self.balance)
acc1=Account(12000,1234)
acc1.debit(5200)
acc1.credit(200)

acc1.print_balance()
# ----------------------------------------------------------------------------------------------------------------------
# question no 55
# define a circle class to create a circle with a radius r using constructor.define an area method() of the class which calculates the area of the circle. define a perimeter() method of the class which  allows you tocalculates the perimeter of the circle
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return (22/7)* self.radius ** 2
    def perimeter(self):
        return 2* (22/7) * self.radius
c1=Circle(21)
print(c1.radius)
print("Area of circle is: ",c1.area())
print("Perimeter of circle is: ",c1.perimeter())
# -----------------------------------------------------------------------------------------------------------------------
# question no 56
# define a employ class with attributes role, department and salary.this class also has a show details() method. create an engineer class that inherits the properties from employee class and has aditional attributes name and age.
class Employee:
    def __init__(self,role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary
    def show_details(self):
        print("Role: ", self.role)
        print("Department: ", self.department)
        print("Salary: ", self.salary)
e1=Employee("accountant", "finance", "60,000")
e1.show_details()
class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super(). __init__("engineer","IT","75,000")
eng1= Engineer("numan",40)
eng1.show_details()
# -----------------------------------------------------------------------------------------------------------------------
# question no 57
# create a class called store which stores the item and its price.use dunder function __gt__ to convey that: order1>order2 if the price of order1 > order2

class Store:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, other):
        return self.price > other.price 
or1=Store("chips",40)
or2=Store("icecream",30) 
print(or1 > or2)
# ------------------------------------------------------------------------------------------------------------------------
# question no 58
# A MINI PROJECT
# guess the number.
import random
random_num= random.randint(1,100)
while True:
    userchoice=(input("enter a number or quit: "))
    if (userchoice == "quit"):
        print("you choose to quit the game")
        break
    userchoice=int(userchoice)
    if (userchoice==random_num):
        print("success!")
        break
    elif (userchoice<random_num):
        print("your guess is too small. Take a bigger guess...")
    else:
        print("your guess is too big. Take a smaller guess...")
    
print("-----Game Over-----")
# --------------------------------------------------------------------------------------------------------------------------
# question no 59
# A MNINI PROJECT
# randon password generator
import random
import string
pass_len = 12
char_val= string.ascii_letters + string.digits + string.punctuation
password= ""
for i in range(pass_len):
    password += random.choice(char_val)
print("your random password is: ",password)
# --------------------------------------------------------------------------------------------------------------------------
