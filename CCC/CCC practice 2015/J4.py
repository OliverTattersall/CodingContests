lines=int(input())
list1=[]
time=[]
time2=0
for i in range(lines):
    x=input()
    a,b=x.split(" ")
    list1.append((a,b))
for i in range(lines):
    if list1[i][0]=="R":
        time.append((list[i][1],time2))
    time2+=1

