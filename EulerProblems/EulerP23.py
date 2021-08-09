### Unsolved

def factorsum(n):
    factors=[1]
    for i in range(2, int(n**(1/2))+1, 1):
        if n%i==0:
            factors.append(i)
            factors.append(n//i)

    return sum(factors)


ab = set()
sums=[]
for i in range(1, 28124, 1):
    item = factorsum(i)
    if item>i:
        ab.add(i)
    sums.append(item)


sumab=set()
# for i in range(len(ab)):
#     for j in range(i, len(ab),1):
#         x=ab[i]+ab[j]
#         if x<28125:
#             sumab.add(x)


# print(sumab)
# all=0
# for i in range(1, 28124):
#     if i not in sumab:
#         all+=i

# print(all)

answer=0
for n in range(1, 28124, 1):
    if sums[n-1]>n:
        sumab.add(n)
    if not any((n - a in sumab) for a in sumab):
        answer+=n

print(answer)

