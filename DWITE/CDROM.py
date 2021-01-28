answers=[]

for i in range(5):
    inp=input().split()
    maxsize=int(inp[0])
    length=int(inp[1])
    for i in range(2, length+2):
        inp[i]=int(inp[i])
    files=sorted(inp[2:])



    grid=[[0 for i in range(maxsize+1)] for i in range(length+1)]

    for i in range(1, length+1):
        for j in range(1, maxsize+1):

            if j>=files[i-1]:

                grid[i][j]=max( files[i-1] + grid[i-1][j-files[i-1]] , grid[i-1][j])

            else:

                grid[i][j]=grid[i-1][j]

    answers.append(grid[-1][-1])

for i in range(5):
    print(answers[i])
                


##check got it right