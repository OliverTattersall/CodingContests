n=int(input())
cheights=input().split()
bheights=input().split()

for i in range(n):
    cheights[i]=int(cheights[i])
    bheights[i]=int(bheights[i])

cheights.sort()

def justStalling(cheights, bheights, n):
    if cheights[-1]>max(bheights):
        return 0
    spots={}
    for i in range(n):
        if cheights[i] not in spots:
            spots[cheights[i]]=0
        for j in range(n):
            if bheights[j]>=cheights[i]:
                spots[cheights[i]]=spots.get(cheights[i], 0)+1

    print(spots)

    def factorial(n):
        product=1
        for i in range(2, n+1, 1):
            product=product*i

        return product

    total = factorial(n)
    fails=0
    for i in range(n):
        fails+= (n-spots[cheights[i]])*factorial(n-1)

    # print(fails, total)

    def finddoubles(hole, val, barns, cows):
        print(val)
        temp = barns[0:hole]+barns[hole+1:]
        temp2 = cows[0:val]+cows[val+1:]
        spots2 ={}

        for i in range(len(temp2)):
            for j in range(len(temp)):
                if temp2[i]<=temp[j]:
                    spots2[temp2[i]]=spots2.get(temp2[i], 0)+1

        # print(spots2)
        if spots2[temp2[-1]]==len(temp2):
            return 0
        for i in range(len(temp2)-1, -1, -1):
            if spots2[temp2[i]]!=len(temp2):
                num=factorial(i)
                print(num, i, temp2, spots2)
                if spots2[temp2[i-1]]!=len(temp2):
                    for j in range(len(temp)):
                        if temp2[i]>temp[j]:
                            print(j, i, temp, temp2, spots2)
                            return finddoubles(j, i, temp, temp2)+num

                # else:
                # print(i)

                return num




        return 0

    doubles=0

    for i in range(n-1, -1, -1):
        if spots[cheights[i]]!=n: 
            if spots[cheights[i-1]]!=n:
                for j in range(n):
                    if cheights[i]>bheights[j]:
                        doubles+=finddoubles(j, i, bheights, cheights)


    # print(doubles)

    return total-fails+doubles


print(justStalling(cheights, bheights, n))