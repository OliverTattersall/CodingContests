

for _ in range(5):
    n = int(input())
    blocks = []
    nums = 0
    for i in range(n):
        temp = input().split(" ")
        blocks.append(list(map(int, temp)))
        nums+=blocks[i][1]
    h = int(input())
    blocks = sorted(blocks)[::-1]
    # print(n, blocks, h, nums)

    lookup={}
    def findBlock(blocks, h, lookup, used, j):
        if j!=float("inf"):
            temp=list(used)
            temp[j]+=1
            used = tuple(temp)
        # print(h)
        if h==0:
            return 0

        if h not in lookup:
            vals=[float("inf")]
            for i in range(len(blocks)):
                if used[i]!=blocks[i][1]:
                    # blocks[i][1]-=1
                    if h-blocks[i][0]>=0:
                        vals.append(findBlock(blocks, h-blocks[i][0], lookup, used, i)+1)
                    else:
                        return float("inf")
                    
            lookup[h]=min(vals)
        return lookup[h]
        # return min(vals)
    print(findBlock(blocks, h, lookup, tuple((0 for i in range(n))), float("inf")))