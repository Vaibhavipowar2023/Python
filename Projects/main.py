import random
def gamewin(comp, you):
    if comp == you: #if two values are equal, declare a tie
        return None
    
    elif comp == "s" : #check for all possiblities when computer chose s
        if you == "w":
            return False
        elif you == "g" :
            return True
        
    elif comp == "w" : #check for all possiblities when computer chose w
       if you == "g":
            return False
       elif you == "s" :
            return True
    
    elif comp == "g" :  #check for all possiblities when computer chose g
        if you == "s":
            return False
        elif you == "w" :
            return True


print("Computer  Turn :Snake(s), Water(w) or Gun(g) ? ")
randNo = random.randint(1,3)
if randNo == 1:
    comp="s"

elif randNo == 2:
    comp = "w"

elif randNo == 3:
    comp = "g"




you = input("Your Turn :Snake(s), Water(w) or Gun(g) ?")
a= gamewin(comp,you)

print(f"Computer choose  : {comp}")
print(f"You choose :{you}")
if a == None:
    print ("The game is tie !")
elif a :
    print ("You win")
else : 
    print("You lost") 