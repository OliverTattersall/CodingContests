n=int(input())
cows=input().split()
barns=input().split()
countcows={}
countbarns={}

for i in range(n):
    barns[i]=int(barns[i])
    cows[i]=int(cows[i])
    countcows[cows[i]]=countcows.get(cows[i], 0)+1
    countbarns[barns[i]]=countbarns.get(barns[i], 0)+1



cows.sort()
barns.sort()
# print(cows, barns)
groups=0
def factorial(n):
    product=1
    for i in range(2, n+1, 1):
        product=product*i

    return product

def findSolution(cows, barns, lookup, lookup2):
    if countbarns==countcows:
        return 1
    
    key=(tuple(cows), tuple(barns))
    if key not in lookup:
        # print(cows, barns)
        if len(cows)==1:
            return 1

        current=cows[-1]
        test=True
        sum=0
        for i in range(len(barns)-1, -1, -1):
            if current<=barns[0]:
                break
            if current<=barns[i]:
                if (current, barns[i]) not in lookup2:

                    z = findSolution(cows[0:-1], barns[0:i]+barns[i+1:], lookup, lookup2)
                    lookup2[(current, barns[i])] = z
                test=False                 
                sum += lookup2[(current, barns[i])]
            else:
                break
        if test:
            sum += factorial(len(cows))
        lookup[key]=sum
    return lookup[key]

lookup={}
lookup2={}
print(findSolution(cows, barns, lookup, lookup2))