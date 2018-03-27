print ('\t\t\t\t\t\t -+=</?>#$% Welcome to the land of Numbers -+=</?>#$%')

number1= int(input("\nEnter an integer number to be added: "))
number2= float(input("Enter a decimal number to be added: "))
number3= float(input("Enter any number to be added: "))

number= number1 + number2 + number3
number= round(number,2)

print("The answer rounded to 2 decimal place is: " + str(number))

input("\nPress ENTER to exit")
