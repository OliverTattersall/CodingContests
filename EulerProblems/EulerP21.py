def factorsum(n):
    factors=set([1])
    for i in range(2, int(n**(1/2))+1, 1):
        if n%i==0:
            factors.add(i)
            factors.add(n//i)

    return sum(factors)


all=0
sums={}

print(factorsum(16))

for i in range(2, 10000):
    if i not in sums:
        item = factorsum(i)
        sums[i]= item
        if item not in sums:
            sums[item] = factorsum(item)

        if i == sums[item] and item!=i:

            all+=i+sums[i]
print(all)

        
