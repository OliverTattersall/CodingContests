numdays=int(input())
firstteam=input().split(" ")
secondteam=input().split(" ")



for i in range(numdays):
    firstteam[i]=int(firstteam[i])
    secondteam[i]=int(secondteam[i])

sum1=sum(firstteam)
sum2=sum(secondteam)


while(True):
    if sum1==sum2:
        break
    else:
        sum1=sum1-firstteam[-1]
        sum2=sum2-secondteam[-1]
        firstteam.pop(-1)
        secondteam.pop(-1)


#def change(first,second, numdays):


print(numdays-(numdays-len(firstteam)))
