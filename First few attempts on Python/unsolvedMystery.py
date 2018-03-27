# Programmer: Leon
print("\t\t\t???Unsolved Mystery Case???")
print("\nThere was a murder in a school called YCIS")
input("\nPress ENTER to see the evidence for this case:")
case={"Evidence":"CCTV",
      "Time":"10",
      "Location":"YCIS",
      "Witness":"Student"}
for x ,  y in case.items():
    print("{0:<10}:{1}".format(x,y))
input("\nPress ENTER to add evidence")
fact=input("Was there any weapons around the place? (Yes/No) ")
print("\nThis is the new evidence:")
case["Weapons"]=fact.title()
for x ,  y in case.items():
    print("{0:<10}:{1}".format(x,y))
print("\nThank you for your help!")