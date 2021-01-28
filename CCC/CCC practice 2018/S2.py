import copy

N=int(input())
flowers=[]
for i in range(N):
    flowers.append(input().split())


double=copy.deepcopy(flowers)

top=[]
right=[]
bottom=[]
left=[]

top=double[0]
bottom=double[-1]

for i in range(N):
    right.append(double[i][-1])
    left.append(double[i][0])



sides=[top, right, bottom, left]


def isincreasing(lst):
    answer=True
    last=int(lst[0])

    for i in range(1, len(lst)):
        if int(lst[i])<last:
            answer=False
            break
        else:
            last=int(lst[i])
    return answer


def test():

    answer=True


    for i in range(4):
        if isincreasing(sides[i]):
            pass
        else:
            answer=False

    return answer


turns=0

for i in range(4):
    # print(flowers, i)
    if test():
        # print(flowers, i)
        break
    else:
        # print(i)

        sides[-1].reverse()
        sides.insert(0, sides[-1])
        sides.pop(-1)
        # sides[-1].reverse()
        sides[-2].reverse()
        turns+=1



answer=[]

if turns==0:
    answer=flowers
elif turns==1:
    for i in range(N):
        temp=[]
        for j in range(N):
            temp.append(flowers[j][i])

        temp2=temp.copy()
        temp2.reverse()
        answer.append(temp2)


elif turns==2:

    for i in range(N-1, -1, -1):
        # print(flowers[i])
        flowers[i].reverse()
        answer.append(flowers[i])

elif turns==3:
    for i in range(N-1, -1, -1):
        temp=[]
        for j in range(N):

            temp.append(flowers[j][i])

        answer.append(temp)



for i in range(len(answer)):
    item=""
    for j in range(len(answer)-1):
        item+=answer[i][j]+" "

    item+=answer[i][-1]
    print(item)


    
