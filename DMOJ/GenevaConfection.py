answers=[]

t=int(input())

for i in range(t):

    N=int(input())
    cars=[]
    for i in range(N):
        cars.append(int(input()))

    cars.reverse()
    branch=[]
    lake=[0]

    while 0 < len(cars):
        if cars[0]==lake[-1]+1:
            lake.append(cars[0])
            cars.remove(cars[0])
        elif len(branch)>0 and branch[-1]==lake[-1]+1:
            lake.append(branch[-1])
            branch.remove(branch[-1])
        else:
            branch.append(cars[0])
            cars.remove(cars[0])

    print(branch)

    for i in range(len(branch)-1,-1, -1):
        if branch[i]==lake[-1]+1:
            lake.append(branch[i])

    


    if len(lake)==N+1:
        answers.append('Y')
    else:
        answers.append("N")
    

for i in range(t):
    print(answers[i])
