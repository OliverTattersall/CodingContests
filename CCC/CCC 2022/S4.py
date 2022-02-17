n, c = list(map(int, input().split(" ")))
places= list(map(int, input().split(" ")))

points={}
for i in range(n):

    points[places[i]] = points.get(places[i], ())+(i+1,)
print(points)
places = list(set(places))
print(places)
triples = set()
x = len(places)
print(x)
for i in range(x):
    # print(i)
    for j in range(x):
        # print(i,j)

        for k in range(x):
            # print(i,j,k)
            if i!=j and i!=k and j!=k:

                w =i
                y =j
                z = k
                # w, y, z = i,j,k
                w,y,z = sorted((w, y, z))
                # if places[z]>c//2 and pla

                if min(c-abs(places[w]-places[y]), abs(places[w]-places[y]))<=c//2:
                    if min(c-abs(places[y]-places[z]), abs(places[y]-places[z]))<=c//2:
                        if min(c-abs(places[w]-places[z]), abs(places[w]-places[z]))<=c//2:
                            continue
                split = places[z]-c//2
                # print(split, w,y,z)
                if (split - places[w]<0 and split-places[y]>0) or (split - places[w]>0 and split-places[y]<0):
                    # print(x,y,z)
                    for l in points[places[w]]:
                        for u in points[places[y]]:
                            for p in points[places[z]]:
                                temp = (l,u,p)
                                temp = tuple(sorted(temp))
                                triples.add(temp)

print(triples, len(triples))