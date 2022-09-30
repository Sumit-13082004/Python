num=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if num>num2:
    great=num
else:
    great=num2
for choice in range(great,num*num2,1):
    if choice%num==0 and choice%num2==0:
        break
else:
    print("The Lcm of %d & %d is %d"%(num,num2,num*num2))
    i=0
if i!=0:
    print("The Lcm of %d & %d is %d"%(num,num2,choice))