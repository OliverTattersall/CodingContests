grid=[]
for i in range(3):
    grid.append(input().split(" "))
#row1=input().split(" ")
#row2=input().split(" ")
#row3=input().split(" ")
#print(grid)

def fix(line):
#    print(line)
#    print(line[0])
#    print(line[1])
#    print(line[2])
    if line.index("X")==0:
        line[0]=int(line[1])+(int(line[1])-int(line[2]))
        #print(line)
        return line
    if line.index("X")==1:
        line[1]=(int(line[0])+int(line[2]))/2
        line[1]=int(line[1])
        #print(line)
        return line
    if line.index("X")==2:
        line[2]=int(line[1])-(int(line[0])-int(line[1]))
        #print(line)
        return line
                


def columnRow(x,y):
    column=[]
    for i in range(3):
        column.append(grid[i][x])
    if grid[y].count("X")==1:
        grid[y]=fix(grid[y])
        return grid
    if column.count("X")==1:
        #print(column)
        column=fix(column)
        for i in range(3):
            grid[i][x]=column[i]
        return grid

def getLoc():
    for x in range(3):
        for y in range(3):
            if grid[y][x]=="X":
                #print(x,y)
                columnRow(x,y)
    for i in range(3):
        if grid[i].count("X")>0:
            getLoc()



xs=[]
nums=[]
for i in range(3):
    xs.append(grid[i].count("X"))
if xs[0]>1 and xs[1]>1 and xs[2]>1:
    for i in range(3):
        for j in range(3):
            if grid[i][j]!="X":
                #print(j)
                nums.append([j,i])
#print(nums)
if len(nums)==1:
    for i in range(3):
        grid[i][nums[0][0]]=grid[nums[0][1]][nums[0][0]]
if len(nums)==2:
    if nums[0][0]!=nums[1][0]:
        for j in range(2):
            for i in range(3):
                grid[i][nums[j][0]]=grid[nums[j][1]][nums[j][0]]
if len(nums)==3:
    if nums[0][0]!=nums[1][0] and nums[0][0]!=nums[1][0] and nums[1][0]!=nums[2][0]:
        for j in range(3):
            for i in range(3):
                grid[i][nums[j][0]]=grid[nums[j][1]][nums[j][0]]
    
#print(grid)        
getLoc()

        

for i in range(3):
    print(str(grid[i][0]) + " "+str(grid[i][1])+ " "+str(grid[i][2]))

