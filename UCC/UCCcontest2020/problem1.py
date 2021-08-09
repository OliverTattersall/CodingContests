num=int(input())
line1=list(input())
line2=list(input())
count=0

for i in range(len(line1)):
    line1[i]=int(line1[i])
    line2[i]=int(line2[i])
    if(line1[i]==0):
        if(line2[i]==0):
            count+=1

print(count)