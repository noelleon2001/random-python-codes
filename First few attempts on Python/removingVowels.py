# This is a program for removing vowels in a sentence
# Program
vowels = "AEIOUaeiou"
sentence = str(input("Enter the sentence below:\n"))
newstr = ''
for character in sentence:
    if character not in vowels:
        newstr += character
print (newstr)

