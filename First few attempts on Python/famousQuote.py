print ('\t\t\t\t\t ---- Welcome to the Printing Shop ----')

quote=input("\nEnter a famous quote below to change the format.\n")

quote1= quote.upper()
quote2= quote.lower()
quote3= quote.title()

print("\nThis is the quote in UPPER CASE: "+ str(quote1))
print("This is the quote in lower case: "+ str(quote2))
print("This is the quote in Title Format: "+ str(quote3))

input("Press ENTER to pay and exit")
