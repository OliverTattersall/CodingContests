measurements=int(input())
value=[]
time=[]
position=[]
for i in range(measurements):
    val=input().split(" ")
    val[0]=int(val[0])
    val[1]=int(val[1])
    time.append(val[0])
    position.append(val[1])
    value.append(val)

value=sorted(value)

# print(value)
maxspeeds=0.0
# print(sorted(value)) 

for i in range(len(value)-1):
    current=abs((value[i+1][1]-value[i][1])/(value[i+1][0]-value[i][0]))
    maxspeeds=max(current, maxspeeds)

print(maxspeeds)


