from collections import deque

n = int(input())
poss=[]
options={}
rockets={}
for i in range(n-1):
    temp=input().split()
    temp[0]=int(temp[0])
    temp[1]=int(temp[1])
    options[temp[0]]=options.get(temp[0], ())+(temp[1],)
    options[temp[1]]=options.get(temp[1], ())+(temp[0],)

    poss.append(temp)


    rockets[tuple(temp)]=False



temp=input().split()

temp[0]=int(temp[0])
temp[1]=int(temp[1])

first = temp.copy()
rockets[tuple(first)]=True
paths = rockets.copy()
points={i+1:False for i in range(n)}

# print(options)

lowerside=0
higherside=0
if len(options[first[0]])!=0:
    points[first[1]]=True

    lowcalc=deque([first[0]])
    while len(lowcalc)!=0:
        
        item = lowcalc.popleft()

        if item in options:
            temp=options[item]
            for i in range(len(temp)):
                if points[temp[i]]!=True:
                    lowerside+=1
                    lowcalc.append(temp[i])
        points[item]=True

# print(lowerside)
if lowerside%2==0:
    points={i+1:False for i in range(n)}
    if len(options[first[1]])!=0:
        points[first[0]]=True

        highcalc=deque([first[1]])
        while len(highcalc)!=0:
            
            item = highcalc.popleft()

            if item in options:
                temp=options[item]
                for i in range(len(temp)):
                    if points[temp[i]]!=True:
                        higherside+=1
                        highcalc.append(temp[i])
            points[item]=True

# print(lowerside, higherside)

if lowerside%2==1 or higherside%2==1:
    print("Let's play >:)")
else:
    print("NOU >:(")