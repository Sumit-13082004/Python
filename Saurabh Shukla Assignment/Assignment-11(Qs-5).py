from itertools import count


cnt=0
for num in range(2,int(input("Enter the how many numbers:"))*2+1,2):
    cnt+=num
print("The sum is",cnt)