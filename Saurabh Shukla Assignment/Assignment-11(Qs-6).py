count=1
fact=int(input("Enter the number for factorial:"))
for num in range(fact,1,-1):
    count*=num
print("The factorial of %d is %d"%(fact,count))