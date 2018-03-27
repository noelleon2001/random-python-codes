# Programmer: Leon
print("\t\t*%!+-Times Table-+!%*")
print("Welcome to the times table generator!")
num=int(input("\nPlease enter a number: "))
for number in range(1,13):
    print("{0} * {1} = {2}".format(number,num,num*number))
print("\nThe {0} times-table has been generated for you!".format(num))
input("\nPress ENTER to exit")