i=3
while i>=1:
    num=int(input("Ener a even number:"))
    i-=1
    if num%2!=0:
        print("Wrong answer. You have %d choice left"%i)
    else:
        print("Congrats, You win the game")
        break
if i==0:
    print("You loose the game")
