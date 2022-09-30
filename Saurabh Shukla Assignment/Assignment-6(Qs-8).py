a,b,c=int(input("Enter the value of co-efficient of x^2:")),int(input("Enter the value of co-efficient of x:")),int(input("Enter the value of constant:"))

if (b**2-4*a*c)>0:
    print("The roots are real & distinct")
elif (b**2-4*a*c)==0:
    print("The roots are real & equal")
else:
    print("The roots are imaginary")
