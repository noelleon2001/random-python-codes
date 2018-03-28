g = ['d','e','f']
cont = True
k =0
for n in range(len(g)):
    if g[n] != 'e' and cont == True:
        k += 1
    elif g[n] == 'e':
        cont = False
print(k)
if position[h] != 'X' and cont == True:
    j += 1
elif position[h] == 'X':
    cont = False
"""
N = 200
Balls_direction = []
collisions = 0
n = -1
while n <= (N-3):
    n += 1
    if Balls_direction[n]=='R' and Balls_direction[n+1]=='L':
        collisions += 1
        Balls_direction[n] = 'L'
        Balls_direction[n+1] = 'R'
        n = -1
print(collisions)


for character in num:

        for character2 in sample[n]:
            print(character2)
            if character2 != character:
                sample.remove(n)
words = []
good_words = 0
for n in range(len(words)):
    c = 0
    vowels = 0
    odd = False
    for character in words[n]:
        c +=1
        if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
            vowels += 1
    if int(c/2) != (c/2):
        odd = True
    if odd == True and vowels >= 3:
        good_words += 1
print(good_words)
#
n = int(input())
c = 1
if n%3 == 0:
    c += 1
if (n+1)%5 == 0:
    c += 2
if (n+2)%7 == 0:
    c += 4
if (n+3)%11 == 0:
    c += 8
if c ==1 :
    c+=16
print(n+c)
"""
