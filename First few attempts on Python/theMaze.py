import time
print ('\t\t\t\t\t ***** Welcome to the Maze Game *****')
print("\nYou are in a maze")
print("You are trying to find your way out!")
print("But you never know how dangerous the maze is.")
input("\nPress ENTER to start!")
print("Starting the maze game, be prepare!!!")
time.sleep(3)
print("\nYou saw an opening and you went into it")
print("You can go forward(f), right(r) or backward(b)")
first= input("\nMake your choice: ")
if first=="f":
    print("\nYou chose f... What will happen?\nYou walk along a corridor...")
    print("...Suddenly, you fell into a hole and died!!!")
    input("\nPress ENTER to exit!")
elif first=="r":
    print("\nYou chose r... What will happen?\nYou saw a zombie running past you...")
    print("...You turn around and saw Cerberus running towards you!!!")
    print("...You ran but you didn't see a trap beside you...\nYou burned to death!!!")
    input("\nPress ENTER to exit!")
elif first=="b":
    print("\nYou chose b... What will happen?\nYou walk back to the starting point...")
    print("...Climb up a ladder and got out of the maze!!!\nYou survived!!!")
    input("\nPress ENTER to exit!")
else:
    print("\nInvalid response")
    first=input("Make your choice: ")
    



