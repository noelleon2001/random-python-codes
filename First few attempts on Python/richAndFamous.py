print ('\t\t\t\t\t\t $$$$$ Welcome to the land of Celebrities $$$$$')

print("\n\t\t\t\t\t\t\t This is to count your monthly expenses!")
print("\n\t\t\t Since you are rich and really famous... ignore the the Jiao in RMB")
print("\t\t\t\t and only enter whole numbers for your monthly expenses in RMB!")

name=input("\nEnter your name, celebrity: ")
name=name.title()
car=int(input("\nPrivate car rental: "))
jet=int(input("Private jet rental: "))
house=int(input("Private house cost: "))
food=int(input("Dining Out: "))
staff=int(input("Staff (slave, chef, driver, assistant): "))
clothing=int(input("Clothing (outwear, uniform, jeans, shirt): "))
games=int(input("Computer games: "))

total= car+jet+house+food+staff+clothing+games
print("\nGrand Total: ${0}".format(total))
print("Good job, {0}! Your spending is below your budget!".format(name))

input("\nPress ENTER to exit")
