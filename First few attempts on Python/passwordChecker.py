# Made by: Leon Chung
print ('\t\t\t\t ^^^^ Welcome to my Website ^^^^')
input("Press ENTER to login.")
print("\nPlease enter your username and password to login!")
username= ""
check=""
password=""
stop=""
turns=3
while turns > 0:
    if username == "ef":
        break
    username = input("\nUsername:")
    if username != "ef":
        turns -= 1
        print ("Incorrect\nTry again.")
        if turns == 0:
            print ("\nSorry, you do not know your username!")
            turns=0
            break
while turns > 0:
    if password == "rr":
        check=""
        break
    password = input("\nPassword:")
    if password != "rr":
        turns -= 1
        print ("Incorrect\nTry again.")
        if turns == 0:
            print ("\nSorry, you do not know your password!")
            turn=0
            break
while turns > 0:
    if check == "109":
        print("Welcome to the website.")
        break
    check = input("\nWhat is 21 + 88? ")
    if check != "109":
        turns -= 1
        print ("Incorrect\nTry again.")
        if turns == 0:
            print ("\nSorry, you do not know how to do math!")
            turn=0
            break






