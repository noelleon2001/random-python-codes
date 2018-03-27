
print ('\t\t\t\t\t\t\t !!!!!!!! Welcome to the land of Artificial Intelligence !!!!!!!')

print ( "\nHello! My name is John")
name1=input('What is your first name?     ')
name1= name1.title()

print ( "\nHello, {0}".format(name1))
name2=input('What is your last name?     ')
name2= name2.title()

print ("\nNice to meet you {0} {1}!".format(name1,name2))

place= input("\nWhere do you live?      ")
place= place.upper()
print ( "\nWow, I live in {0} too!".format(place))
print ("We came from the same planet!!!")

age= int(input("\nWhat is your age?       "))
if age<15:
    print ("Wow, you are still young!")
elif age>15:
    print ("Wow, you are older than me!")
else:
    print ("Wow, you are the same age as me!")

input("\nPress ENTER to exit")
print ("Thank you for talking with me! \n Hope to see you again!")