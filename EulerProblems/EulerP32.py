prods = set()

for i in range(1, 10000, ):
    for j in range(1, 100, 1):
        total = str(i)+str(j)+str(i*j)
        temp = set(list(total))
        if len(temp)==9 and '0' not in temp and len(total)==9:
            # print(temp)
            prods.add(i*j)
            # print()

# print(prods)
# print(len(prods))
prods=list(prods)
sum =0
for i in prods:
    sum+=i
print(sum)