string=str(input("Enter a string:"))
if string.count(' ')>0:
    pass
match 1 if string.count(' ')>0 else 2:
    case 1:
        print("Multiword string")
    case 2:
        print("Single line string")
