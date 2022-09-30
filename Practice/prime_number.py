num=int(input("Enter a number:"))
i=0
for check in range(2,num,1):
    if num%check==0:
        break
else:
    print("It is Prime number")
    i+=1
if i==0:
    print("It is not a Prime number")
