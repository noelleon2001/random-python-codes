list = [1,3,2,2,4,5,8,6,10000000000]
final_list = []
for q in list:
    if q not in final_list and 0<q<=1000000:
        final_list.append(q)
print(final_list)
