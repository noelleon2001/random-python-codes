# Programmer: Leon
import random
print("\t\t???Average Numbers???")
number=0
no=0
for num in range(0,7):
    num=random.randint(1,100)
    print (str(num))
    number += num
    no+=1
print("\nTotal number = "+str(number))
average= number/no
average= round(average,2)
print (average)