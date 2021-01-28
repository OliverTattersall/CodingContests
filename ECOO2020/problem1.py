key=['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C']
cases=[]
solution=[]
count=0
num=int(input())
for i in range(num):
    a=input().split(" ")
    cases.append(a)



for i in range(num):
    solution.append([0,0])


for i in range(num):
    for j in range(4):
        if j!=0:
            a=cases[i][0]
            b=cases[i][1]
            c=cases[i][2]
            d=cases[i][3]
            cases[i][0]=d
            cases[i][1]=a
            cases[i][2]=b
            cases[i][3]=c
        if solution[i][0]!=3:
            for k in range(len(key)):
                if cases[i][0]==key[k]:
                    if k>3 and k<len(key)-4:
                        if cases[i][1]==key[k-4] or cases[i][1]==key[k+4]:
                            count+=1
                    elif k<=3:
                        if cases[i][1]==key[len(key)-(5-k)] or cases[i][1]==key[k+4]:
                            count+=1
                    elif k>=len(key)-4:
                        if cases[i][1]==key[k-4] or cases[i][1]==key[(len(key)-k)]:
                            count+=1
                if cases[i][1]==key[k]:
                    if k>2 and k<len(key)-3:
                        if cases[i][2]==key[k-3] or cases[i][2]==key[k+3]:
                            count+=1
                    elif k<=2:
                        if cases[i][2]==key[len(key)-(4-k)] or cases[i][2]==key[k+3]:
                            count+=1
                    elif k>=len(key)-3:
                        if cases[i][2]==key[k-3] or cases[i][2]==key[(len(key)-k)]:
                            count+=1
                if cases[i][2]==key[k]:
                    if k>2 and k<len(key)-3:
                        if cases[i][3]==key[k-3] or cases[i][3]==key[k+3]:
                            count+=1
                    elif k<=2:
                        if cases[i][3]==key[len(key)-(4-k)] or cases[i][3]==key[k+3]:
                            count+=1
                    elif k>=len(key)-3:
                        if cases[i][3]==key[k-3] or cases[i][3]==key[(len(key)-k)]:
                            count+=1
                if k==len(key)-1:
                    solution[i][0]=count
                    solution[i][1]=j
                    # solution.append([count,0])
                    count=0



for i in range(num):
    if solution[i][0]==3:
        if solution[i][1]==0:
            print("root")
        elif solution[i][1]==1:
            print("first")
        elif solution[i][1]==2:
            print("second")
        elif solution[i][1]==3:
            print("third")
    else:
        print("invalid")