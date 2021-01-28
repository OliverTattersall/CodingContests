n, q = input().split()
n=int(n)
q=int(q)

alphabet=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

fence=input()

segments=[]

places=[]



for i in range(q):

    temp=input().split()
    segments.append([int(temp[0]), int(temp[1])])

    item2=[fence[0:segments[i][0]-1],fence[segments[i][1]:]]
    # print(item2)

    places.append(item2)

print(places, segments)

for i in range(q):
    sum = 0
    for j in range(len(places[i])):
        temp=places[i][j]
        if places[i][j]=="":
            continue
        
        past=[0 for i in range(len(places[i][j]))]
        past[0]=1
        
        for k in range(1, len(places[i][j])):
            if ord(places[i][j][k])<=ord(places[i][j][k-1]):
                past[k]=past[k-1]
            elif ord(temp[k])>ord(temp[k-1]):
                past[k]=past[k-1]+1
        sum+=past[-1]
    print(sum)
