# Programmer: Leon
print("\t\t!!!Geography Quiz!!!")
input("Press ENTER to start the quiz")
ans=input("\nWhat is the capital of China? ")
ans=ans.title()
correct=0
while correct == 0:
    if ans == "Beijing":
        print("Correct! Well done!")
        correct=1
        break
    else:
        ans=input("Incorrect! Try again: ")
        ans=ans.title()

input("\nPress ENTER to see the next question")
ans=input("\nWhat is the capital of Japan? ")
ans=ans.title()
correct=0
while correct == 0:
    if ans == "Tokyo":
        print("Correct! Well done!")
        correct=1
        break
    else:
        ans=input("Incorrect! Try again: ")
        ans=ans.title()

input("\nPress ENTER to see the next question")
ans=input("\nWhat is the capital of Malaysia? ")
while ans != "Kuala Lumpur":
    ans=input("Incorrect! Try again: ")
    ans=ans.title()
    break
print("Correct! Well done!")


