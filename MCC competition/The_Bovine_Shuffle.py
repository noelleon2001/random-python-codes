# Programmer: Chung Chin Leon
# Date: 2017/12/16

# Program

import sys
sys.stdin = open("shuffle.in","r")
sys.stdout = open("shuffle.out","w")

n = int(input())
a = input().split(" ")
ID = input().split(" ")
new = []
for i in range(n):
    new.append(a[i]+ID[i])
new.sort()
for s in range(n):
    print(new[s][1:])

'''
cows = {}
n = int(input())
a = input().split(" ")
ID = input().split(" ")
for i in range(n):
    cows[ID[i]] = a[i]
for key in sorted(cows, key = cows.get):
    print (key)
'''
