import random
def game(comp,you):
    if comp==you:
        return None
    elif comp=='s':
        if you=='w':
            return False
        else:
            return True
    elif comp=='w':
        if you=='g':
            return False
        else:
            return True
    elif comp=='g':
        if you=='s':
            return False
        else:
            return True



print("Computer's turn: Snake(s) Water(w) Gun(g)?")
rand_no=random.randint(1,3)
if rand_no==1:
    comp='s'
elif rand_no==2:
    comp='w'
elif rand_no==3:
    comp='g'

you=input("Your turn: Snake(s) Water(w) Gun(g)?")
print("Computer entered:",comp)
print("You entered:",you)
a=game(comp,you)
if a==None:
    print("Its a tie 2 more chances")
elif a==True:
    print("You Win!")
else:
    print("You Lose!")

if a==None:
    print("Computer's turn: Snake(s) Water(w) Gun(g)?")
    rand_no=random.randint(1,3)
    if rand_no==1:
        comp='s'
    elif rand_no==2:
        comp='w'
    elif rand_no==3:
        comp='g'

    you=input("Your turn: Snake(s) Water(w) Gun(g)?")
    print("Computer entered:",comp)
    print("You entered:",you)
    a=game(comp,you)
    if a==None:
        print("Its a tie 1 more chance")
    elif a==True:
        print("You Win!")
    else:
        print("You Lose!")
    if a==None:
        print("Computer's turn: Snake(s) Water(w) Gun(g)?")
        rand_no=random.randint(1,3)
        if rand_no==1:
            comp='s'
        elif rand_no==2:
            comp='w'
        elif rand_no==3:
            comp='g'

        you=input("Your turn: Snake(s) Water(w) Gun(g)?")
        print("Computer entered:",comp)
        print("You entered:",you)
        a=game(comp,you)
        if a==None:
            print("Its a tie, you think alike!!")
        elif a==True:
            print("You Win!")
        else:
            print("You Lose!")



