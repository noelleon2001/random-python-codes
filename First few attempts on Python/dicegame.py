import random
print("\t\t+++Dice game+++")
die1= random.randint(1, 6)
die2= random.randint(1, 6)
die3= random.randint(1, 6)
print("\nNumber for the first dice is "+str(die1))
print("Number for the second dice is "+str(die2))
print("Number for the third dice is "+str(die3))
if die1==die2==die3:
    score=die1+die2+die3
elif die1==die2:
    score=die1+die2-die3
elif die1==die3:
    score=die1+die3-die2
elif die2==die3:
    score=die2+die3-die1
else:
    score=0
print("\nYour score is "+str(score))

print("\nInput a number between 1 and 6!")
for num in range(1,6):
    num=die1 or die2 or die3
    if num not in range(1,6):
        print("You did not input a number between 1 and 6")
    die1=int(input("Number for the first dice: "))
    die2=int(input("Number for the second dice: "))
    die3=int(input("Number for the third dice: "))

    if die1==die2==die3:
        score=die1+die2+die3
    elif die1==die2:
        score=die1+die2-die3
    elif die1==die3:
        score=die1+die3-die2
    elif die2==die3:
        score=die2+die3-die1
    else:
        score=0


print("\nYour score is "+str(score))