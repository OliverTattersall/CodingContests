def factorial(n):
    if n==1 or n==0:
        return 1
    return n*factorial(n-1)

dct ={}

sum = 0
for i in range(10000000):
    x = str(i)
    temp = 0
    for j in x:
        j = int(j)
        if j not in dct:
           dct[j] = factorial(j)
        temp+=dct[j]

        # print()
    if temp == i:
        sum+=temp

print(sum-3)