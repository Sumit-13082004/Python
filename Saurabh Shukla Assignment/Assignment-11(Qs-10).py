count=0
val=0
num=int(input("Enter a number:"))
while(num>0):
    val=val*10+(num%8)
    num//=8
while(val>0):
    count=count*10+(val%10)
    val//=10
print("The octal format is",count)
