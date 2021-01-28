n=int(input())
nums=input().split()
for i in range(n):
    nums[i]=int(nums[i])

evens=[]
odds=[]

for i in range(n):
    if nums[i]%2==0:
        evens.append(nums[i])
    else:
        odds.append(nums[i])

groups=0




if len(evens)>=len(odds):
    groups+=len(odds)*2
    if len(evens)-len(odds)>0:
        groups+=1

elif len(odds)>len(evens):
    temp=len(odds)-len(evens)
    groups+=len(evens)*2
    if (len(odds)-len(evens))%3==0 or (len(odds)-len(evens)+1)%3==0:
        

        if temp%3==0:
            groups+=(temp//3)*2

        else:
            groups+=(temp//3)*2+1

    elif temp==1:
        groups+= - 2

    elif temp==4:
        groups+=0

    else:
        groups+=((temp-1)//3)*2-1




    

print(groups)

