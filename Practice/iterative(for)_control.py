'''i=0
for check in input("Enter a string:"):
    if(check=='a'):
        i+=1
print(i)'''
#print("The apple-{}".format(input("Enter a string").count('apple')))
for choice in input("Enter a string:"):
    if choice!='r'and choice!='R':
        print(choice,end='')
    else:
        break
else:
    print()
    print("Successfully Printed")

    