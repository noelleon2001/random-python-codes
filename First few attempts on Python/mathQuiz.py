# Made by: Leon Chung
print ('\t\t ***** Math Quiz *****')
print("\nPlease answer the math questions below")
print("and see how many questions will answer correctly!!!")
print("\n(Don't use a calculator!)")
input("Press ENTER to start")
print("\nQuestion 1")
ans=input("What is 13 * 20? ")
if ans == "260":
    print("Correct")
    ans1= 1
else :
    print("Incorrect")
    print("The correct answer is 260!")
    ans1= 0
input("Press ENTER to start the next question")

print("\nQuestion 2")
ans=input("What is 34 * 22? ")
if ans == "748":
    print("Correct")
    ans2= 1
else :
    print("Incorrect")
    print("The correct answer is 748!")
    ans2= 0
input("Press ENTER to start the next question")

print("\nQuestion 3")
ans=input("What is 58 * 21? ")
if ans == "1218":
    print("Correct")
    ans3= 1
else :
    print("Incorrect")
    print("The correct answer is 1218!")
    ans3= 0

total=ans1+ans2+ans3
print("\nGood Job! You answered {0} correct questions!".format(total))
print("\nThank you for doing the math quiz!")
input("Press ENTER to exit")

