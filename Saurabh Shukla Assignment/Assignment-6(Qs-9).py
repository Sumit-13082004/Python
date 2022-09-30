year=int(input("Enter a year:"))
print("%d is a leap year"%year) if (year%400==0) or (year%4==0 and year%100!=0) else print("%d is not a leap year"%year)
