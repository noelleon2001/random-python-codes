import os
import time
import random

print ('\t\t\t\t\t\t ????? Welcome to the MAGIC BALL game ?????')
os.system("say 'welcome to my magic ball game'")
os.system("say 'type your name and press enter to find out your future'")
input("\nType your name and press ENTER to find out your future: ")
time.sleep(1)
print("\nShaking...")
time.sleep(3)

n=random.randint(1, 8)
if n==1:
    print("\nYou will get a very good job in the future.")
    os.system("say 'You will get a very good job in the future'")
elif n==2:
    print("\nYou will have ten children.")
    os.system("say 'You will have ten children'")
elif n==3:
    print("\nYou will never get married.")
    os.system("say 'You will never get married'")
elif n==4:
    print("\nYou might get an F in the next test.")
    os.system("say 'You might get an F in the next test'")
elif n==5:
    print("\nYou might die in the age of 50.")
    os.system("say 'You might die in the age of fifty'")
elif n==6:
    print("\nYou will live a long live.")
    os.system("say 'You will live a long live'")
elif n==7:
    print("\nYou will be cursed.")
    os.system("say 'You will be cursed'")
elif n==8:
    print("\nYou will have no future generation.")
    os.system("say 'You will have no future generation'")

