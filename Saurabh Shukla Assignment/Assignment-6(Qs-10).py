num1,num2,num3=eval(input("Enter first number:")),eval(input("Enter second number:")),eval(input("Enter third number:"))
if num1>=num2 and num1>=num3:
    print("%d is greater number"%num1)
elif num2>=num3:
    print("%d is greater number"%num2)
else:
    print("%d is greater number"%num3)
    