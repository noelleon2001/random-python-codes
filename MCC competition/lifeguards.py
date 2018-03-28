import sys
sys.stdin = open("lifeguards.in","r")
sys.stdout = open("lifeguards.out","w")
def overlap(a,b):
    x2 =0
    x1 =0
    if a[0] > b[0]:
        x1 = b[0]
    if b[0] >= a[0]:
        x1 = a[0]
    if a[1] > b[1]:
        x2 = b[1]
    if b[1] >= a[1]:
        x2 = a[1]
    a = [x1,x2]
    return a
with open('lifeguards.in') as a:
    content = a.readlines()
content = [x.strip().split(' ') for x in content]
del content[0]
content = sorted(content)
maxd = 0
final_list=[]
for n in range(len(content)-1):
    final_list.append(overlap(content[n],content[n+1]))
for n in range(len(final_list)):
    # case1
    diff = int(content[n][1]) - int(content[n][0])
    if diff > maxd:
        maxd += diff
print(maxd)
