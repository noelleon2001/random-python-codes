# Programmer: Chung Chin Leon
# Date: 2017/12/16

# Program
import sys
sys.stdin = open("measurement.in","r")
sys.stdout = open("measurement.out","w")
n = int(input())
sort = []
m = 7
e = 7
b = 7
x = 7
strout = 0
for i in range(n):
    str = input()
    sort.append(str)
sort.sort()
for o in range(n):
    c = sort[o].split(' ')
    if c[1] == 'Mildred':
        m += int(c[2])
    elif c[1] == 'Elsie':
        e += int(c[2])
    elif c[1] == 'Bessie':
        b += int(c[2])
    if m > x or e > x or b > x:
        strout += 1
        if m>x:
            x = m
        elif b>x:
            x = b
        elif e>x:
            x = e
    elif x in (m,b,e):
        strout += 1
print(strout)
