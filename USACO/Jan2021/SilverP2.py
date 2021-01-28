n, q = input().split()
n=int(n)
q=int(q)

alphabet=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

fence=input()

segments=[]
letters=dict()
places=[]


for i in range(q):

    temp=input().split()
    segments.append([int(temp[0]), int(temp[1])])

    item2=[fence[0:segments[i][0]-1],fence[segments[i][1]:]]
    # print(item2)

    places.append(item2)



def paint(sec, lookup, origin):
    global letters

    key=sec

    # for j in range(len(sec)):
    if key not in lookup:
        if key[::-1] not in lookup:
            # print(letters[origin], sec)
            lightest=list(letters[origin])[0]
            # print(lightest, letters[origin], sec)
            letters[origin].remove(lightest)

            # lightest=""
            # for k in range(26):
            #     if alphabet[k] in sec:
            #         lightest=alphabet[k]
            #         break

            temp=sec.split(lightest)
            # print(temp)
            sum=0
            for i in range(len(temp)):
                sum+=paint(temp[i], lookup, origin)
            lookup[key]= sum+1
        else:
            lookup[key]=lookup[key[::-1]]
    return lookup[key]



lookup={"":0}
for i in range(q):
    sum1=0
    for j in range(len(places[i])):
        temp=set([])
        for k in range(len(places[i][j])):

            temp.add(places[i][j][k])
        letters[places[i][j]]=sorted(temp)
        # print(places[i][j], j)
        sum1+=paint(places[i][j], lookup, places[i][j])

    print(sum1)

# print(paint("AB")+paint("CB"))