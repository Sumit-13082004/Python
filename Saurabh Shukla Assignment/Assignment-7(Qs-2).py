#Write a menu driven program to perform following operations - Addition, Subtraction,Multiplication, Division
import os
print("It is a simple calculator")
print("Here you can do Addition, Subtraction,Multiplication, Division.Press exit to end")

while 1:
    choice=str(input("Enter your choice:"))
    match choice:
        case '+':
            num1,num2=eval(input("Enter first number")),eval(input("Enter second number"))
            print(num1+num2)
        case '-':
            num1,num2=eval(input("Enter first number")),eval(input("Enter second number"))
            print(num1-num2)
        case '*':
            num1,num2=eval(input("Enter first number")),eval(input("Enter second number"))
            print(num1*num2)
        case '/':
            num1,num2=eval(input("Enter first number")),eval(input("Enter second number"))
            print(num1/num2)
        case 'exit':
            break
        case _:
            print("Enter right choice")
    input()
    os.system('cls') 

        