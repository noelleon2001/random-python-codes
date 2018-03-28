import sys
sys.stdin = open("outofplace.in","r")
sys.stdout = open("outofplace.out","w")
num = int(input())-1
with open('outofplace.in') as a:
    content = a.readlines()
content = [int(x.strip()) for x in content]
del content[0]
final_list = []
for q in content:
    if q not in final_list and 0<q<=1000000:
        final_list.append(q)

origin = sorted(final_list)

i = 0
while origin != final_list:
    for n in range(len(final_list)-1):
        if final_list[n] > final_list[n+1]:
            a, b = final_list.index(final_list[n]), final_list.index(final_list[n+1])
            final_list[b], final_list[a] = final_list[a], final_list[b]
            i += 1
print(int(i))

