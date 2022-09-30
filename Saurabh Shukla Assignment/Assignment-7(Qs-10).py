import imp
from colorama import Fore,Back,Style
fav_color=str(input("Enter your favorite color:"))
if fav_color.count("yellow"):
    choice=1
elif fav_color.count("blue"):
    choice=2
elif fav_color.count("orange"):
    choice=3
elif fav_color.count("white"):
    choice=4
elif fav_color.count("black"):
    choice=5
elif fav_color.count("red"):
    choice=6
else:
    choice='_'

match choice:
    case 1:
        print(Fore.YELLOW+"Yellow-Monday")
    case 2:
        print(Fore.BLUE+"Blue-Tuesday")
    case 3:
        print(Fore.CYAN+"Orange-Wednesday")
    case 4:
        print(Fore.WHITE+"White-Thursday")
    case 5:
        print(Fore.BLACK+"Black-Friday")
    case 6:
        print(Fore.RED+"Red-Saturday")
    case _:
        print(Fore.MAGENTA+"All other colours-Sunday")
      
