n, q = input().split()
n=int(n)
q=int(q)

alphabet=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

fence=input()
segments=[]
blanks=[]
places=[]
smallest=[]
for i in range(q):
    smallest.append(float("inf"))
    temp=input().split()
    segments.append([int(temp[0]), int(temp[1])])
    item = fence[segments[i][0]-1:segments[i][1]]
    item2=[fence[0:segments[i][0]-1],fence[segments[i][1]:]]
    # print(item2)
    blanks.append(item)
    places.append(item2)

# print(segments, blanks, places)

def paint(sec, lookup):
    key=sec
    if sec=="":
        return 0
    # for j in range(len(sec)):
    if key not in lookup:
        if key[::-1] not in lookup:
            lightest=""
            # min=float("inf")
            # for i in range(len(sec)):
            #     item=ord(sec[i])
            #     if item<min:
            #         min=item
            # lightest=chr(min)

            for k in range(26):
                if alphabet[k] in sec:
                    lightest=alphabet[k]
                    break

            temp=sec.split(lightest)
            # print(temp)
            sum=1
            for i in range(len(temp)):
                sum+=paint(temp[i], lookup)
            lookup[key]= sum
        else:
            lookup[key]=lookup[key[::-1]]
    return lookup[key]



lookup={}
for i in range(q):
    sum1=0
    for j in range(len(places[i])):
        # print(places[i][j], j)
        sum1+=paint(places[i][j], lookup)

    print(sum1)

# print(paint("AB")+paint("CB"))