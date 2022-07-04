i = 1
round = (input(print("enter the number of rounds you want to play?\t")))
round = int (round)
while i < round+1 :

    import random

    num= random.randint(1,3)
    i = i+1
    if(num==1):
        comp = 's'
    elif(num==2):
        comp = 'p'
    elif(num ==3):
        comp = 's'

    you = input("choose your option, stone(s), paper(p), scissors(sc)?\n")
    if(you == comp):
        print("match draw. computer chose", comp, "and player chose", you)
    elif(you == 's' and comp == 'p' ):
        print("player wins. computer chose", comp, "and player chose", you)    
    elif(you == 's' and comp == 'sc' ):
        print("player wins. computer chose", comp, "and player chose", you)    
    elif(you=='p' and comp =='sc'):
        print("computer wins. computer chose", comp, "and player chose", you)
    elif(you=='p' and comp =='s'):
        print("computer wins. computer chose", comp, "and player chose", you)
    elif(you == 'sc' and comp == 's'):
        print("computer wins. computer chose", comp, "and player chose", you)
    elif(you == 'sc' and comp == 'p'):
        print("player wins. computer chose", comp, "and player chose", you)
    else:
        print("wrong value entered")
print("game over. Thanks for playing.")
