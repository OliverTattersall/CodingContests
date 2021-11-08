# incomplete

dct= {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9}

grid=[]
end = [["*" for _ in range(9)] for _ in range(10)]

for i in range(10):
    temp = input().split()
    grid.append(temp)


## change 2d list as going along
def findVal(xy):
    y2 = dct[xy[0]]
    x2 = int(xy[1])-1
    sum=0
    if grid[y2][x2].isdigit():
        return int(grid[y2][x2])
    else:
        temp2 = xy.split("+")
        for i in range(len(temp2)):
            sum+=findVal(temp2[i])
        
    return sum



for y in range(10):
    for x in range(9):
        
        if grid[y][x].isdigit():
            end[y][x] = int(grid[y][x])
        else:
            temp = grid[y][x].split("+")
            val = 0
            for i in range(len(temp)):
                val+=findVal(temp[i])
            end[y][x]=val


print(end)