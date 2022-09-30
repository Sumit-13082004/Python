from colorama import Fore,Back,Style
count=0
for num in str(input(Fore.RED+Style.BRIGHT+'Enter a number:')):
    count+=1
print(Fore.WHITE+Style.NORMAL+"The digit is %d"%count)
