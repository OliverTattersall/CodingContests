nums = input().split()
walks = {}
for i in range(int(nums[1])):
    temp=input().split()
    walks[int(temp[0])] = int(temp[1])

switches = []
current = input().split()
for i in range(int(nums[2])):
    temp=input().split()
    temp[0] = int(temp[0])
    temp[1] = int(temp[1])
    switches.append(temp)

for i in range(len(current)):
    current[i] = int(current[i])


# print(walks, switches, current)

def solve(cur, loc, i, lookup, count):
    # print(loc, i)
    if count>994:
        return float("inf")
    
    if loc == len(cur):
        return 0

    if loc not in lookup:

        # visited.add(loc)
        if i+1 ==len(cur):
            train=float("inf")
        else:
            train = solve(cur, cur[i+1], i+1, lookup, count+1)+1

        if loc not in walks:
            walk = float("inf")
        
        else:
            if loc not in lookup:
                walk = solve(cur, walks[loc], cur.index(walks[loc]), lookup, count+1)+1
            else:
                walk = float("inf")

        lookup[loc] = min(train, walk)

    return lookup[loc]




for i in range(int(nums[2])):
    lookup={}
    visited = set()
    temp = current.copy()
    x = temp[switches[i][0]-1]
    y = temp[switches[i][1]-1]
    temp[switches[i][0]-1]=y
    temp[switches[i][1]-1] = x
    current = temp.copy()
    x = solve(current, 1, 0, lookup, 0)
    print(x)
    
