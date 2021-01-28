N, M=input().split()
N=int(N)
M=int(M)
grid=[]

for i in range(N):
    grid.append(input())

def testdot(x, y, count):
    if x==0:
        print()
    elif x==N-1:
        print()

    elif y==0:
        print()

    elif y==M-1:
        print()

    else:

        # print(x,y)
        if grid[x-1][y]=="S" or grid[x+1][y]=="S" or grid[x][y-1]=="S" or grid[x][y+1]=="S":
            return count+1

        if grid[x-1][y]!="W":
            return testdot(x-1, y, count+1)
        if grid[x+1][y]!="W":
            return testdot(x+1, y, count+1)
        if grid[x][y-1]!="W":
            return testdot(x, y-1, count+1)
        if grid[x][y+1]!="W":
            return testdot(x, y+1, count+1)

        if grid[x-1][y]=="W" and grid[x+1][y]=="W" and grid[x][y-1]=="W" and grid[x][y+1]=="W":
            return -1

        


for i in range(N):
    for j in range(M):
        if grid[i][j]==".":
            print(testdot(i, j, 0))

