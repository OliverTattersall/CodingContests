
def createTree(tree, arr, pos, i, j):
    ranges[pos] = [i, j]
    n=len(arr)

    if len(arr)==1:
        tree[pos] = arr[0]
        return

    if n%2==0:
        createTree(tree, arr[0:n//2], 2*pos+1, i+0, i+n//2-1)
        createTree(tree, arr[n//2:], 2*pos+2, i+n//2, i+n-1)
    else:
        createTree(tree, arr[0:n//2+1], 2*pos+1, i+ 0, i+ n//2)
        createTree(tree, arr[n//2+1:], 2*pos+2, i+ n//2+1, i+ n-1)
    tree[pos]=min(tree[2*pos+1], tree[2*pos+2])
    


def findQuery(i, j, pos=0):
    if i<=ranges[pos][0] and j>=ranges[pos][1]:
        return tree[pos]
    elif i>ranges[pos][1] or j< ranges[pos][0]:
        return float("inf")
    else:
        return min(findQuery(i, j, 2*pos+1), findQuery(i, j, 2*pos+2))



arr = [-1, 0, 5, 6, 7]
n=len(arr)
div = 0

while n!=1:
    n=n//2
    div+=1

n=len(arr)
rem = n - 2**div
print(div,rem)

tree = [0 for i in range(2**(div+1) -1 + 2*rem)]
ranges=[[0,0] for i in range(2**(div+1)-1+2*rem)]
print(tree, len(tree))

createTree(tree, arr, 0, 0, n-1)
print(tree)
print(ranges)



    

print(findQuery(2, 4, 0))