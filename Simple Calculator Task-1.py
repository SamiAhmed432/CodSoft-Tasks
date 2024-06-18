# Wrtiting a Python program to implement simple calculator using arithmetic operator
from random import choice

def add(x,y):        #This function Adds two numbers
    return x+y

def subtract(x,y):   #This function Subtracts two numbers 
    return x-y

def multiply(x,y):   #This function Multiplies two numbers
    return x*y

def divide(x,y):    #This function Divides two numbers
    return x/y

print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiple")
print("4.Divide")

while True:
  choice=input("Enter choice(1/2/3/4): ")

  if choice in('1','2','3','4',):
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))

        if choice =='1':
            print(num1,"+",num2,"=",add(num1,num2))

        elif choice =='2':
             print(num1,"-",num2,"=",subtract(num1,num2))

        elif choice =='3':
             print(num1,"*",num2,"=",multiply(num1,num2))

        elif choice =='4':
             print(num1,"/",num2,"=",divide(num1,num2))

else:
    print("Invalid input")