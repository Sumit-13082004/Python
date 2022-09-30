year=int(input("Enter the month number:"))
match year:
    case 1:
        print("January-31days")
    case 2:
        print("February-28days")
    case 3:
        print("March-31days")
    case 4:
        print("April-30days")
    case 5:
        print("May-31days")
    case 6:
        print("June-30days")
    case 7:
        print("July-31days")
    case 8:
        print("August-31days")
    case 9:
        print("September-30days")
    case 10:
        print("October-31days")
    case 11:
        print("November-30days")
    case 12:
        print("December-31days")
    case _:
        print("Please enter correct number")
    