# Snake Water Gun
import random
lst=['s','w','g']
chance=5
no_of_chance=0
computer_point=0
user_point=0

print("\t\t\tSnake, Water, Gun\n\n")
print("s for snake\nw for water\ng for gun")

while no_of_chance<chance:
    user=input("Chosse any one Snake,Water,Gun\n")
    comp=random.choice(lst)

    if comp==user:
        print("Both given 0 point to each\n")
        print(f"Computer guess {comp} and User guess {user}")
        print("Tie!")
        print(f"Computer point {computer_point} and User point {user_point}")

    elif comp=='s':
        if user=='w':
            computer_point+=10
            print(f"Computer guess {comp} and User guess {user}")
            print("Computer Win!")
            print(f"Computer point {computer_point} and User point {user_point}")
        if user=='g':
            user_point+=10
            print(f"Computer guess {comp} and User guess {user}")
            print("User Win!")
            print(f"Computer point {computer_point} and User point {user_point}")

    elif comp=='w':
        if user=='s':
            user_point+=10
            print(f"Computer guess {comp} and User guess {user}")
            print("User Win!")
            print(f"Computer point {computer_point} and User point {user_point}")
        if user=='g':
            computer_point+=10
            print(f"Computer guess {comp} and User guess {user}")
            print("Computer Win!")
            print(f"Computer point {computer_point} and User point {user_point}")

    elif comp=='g':
        if user=='s':
            computer_point+=10
            print(f"Computer guess {comp} and User guess {user}")
            print("Computer Win!")
            print(f"Computer point {computer_point} and User point {user_point}")
        if user=='w':
            user_point+=10
            print(f"Computer guess {comp} and User guess {user}")
            print("User Win!")
            print(f"Computer point {computer_point} and User point {user_point}")

    else:
        print("Plz enter valid option")

    no_of_chance+=1
    print(f"{chance-no_of_chance} left out of {chance}")



print("Game Over!!")
print(f"Computer point {computer_point} and User point {user_point}")
if computer_point==user_point:
    print("Game Tie!")
elif computer_point>user_point:
    print("Computer Win!")
else:
    print("You Win!")