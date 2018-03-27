import random
tries=0
print("\t\t\tMultiplication Tables Test")
num=int(input("\nWhat table would you like to be tested on?" ))
print("You will be given 5 questions!")
input("\nPress ENTER to start")
for ans in range(0,5):
    number=random.randint(1,20)
    ans=int(input("\n{0} * {1} = ".format(num,number)))
    if ans!=num*number:
        print("Incorrect")
        print("The correct answer is {0}".format(num*number))
    else:
        print("Correct")
        tries +=1
print("\nYou score is {0} out of 5".format(tries))
if tries==5:
    print("You are a math genius")
elif tries ==4:
    print("You are quite good in math")
else:
    print("You should go back to the first grade")