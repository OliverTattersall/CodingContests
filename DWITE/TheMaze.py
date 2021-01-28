answers=[]

for i in range(1):

    height, width=input().split()
    width=int(width)
    height=int(height)

    grid=[]
    for i in range(height):
        
        grid.append(input())


    def travel(x, y, lookup):
        print(x, y)
        
        key=(y, x)
        if (y, x) not in lookup:
            # print("\n")
            # print(y, x, grid[y][x])
            if grid[y][x]=="#" or grid[y][x]=="X":

                return float("inf")

            else:

                if grid[y][x-1]=="E" or grid[y][x+1]=="E" or grid[y+1][x]=="E" or grid[y-1][x]=="E":
                    # print(key)
                    return 0

                else:
                    lookup[key]=0
      

                    lookup[key] = min(travel(x, y+1, lookup), travel(x, y-1, lookup) , travel(x+1, y, lookup) , travel(x-1, y, lookup))+1

        else:
            return float("inf")

        return lookup[key]

        

    lookup={}

    for i in range(height):

        for j in range(width):

            if grid[i][j]=="X":


                print(travel(j, i-1, lookup))

    print(lookup)



## not done
