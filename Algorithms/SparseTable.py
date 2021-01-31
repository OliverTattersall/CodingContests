import math
import time

def createTable(arr, n, nums):
    width = int(math.log(n, 2))
    # print(width)
    
    for i in range(n):
        arr[i][0]=i

    for j in range(1, width+1):
        # print(arr)
        for i in range(n):
        
            num = 2**j
            num2 = 2**(j-1)
            if i+num-1<=n-1:
                # print(arr[i][j-1], arr[i+num2][j-1], i, j, num2)
                # print(nums[arr[i][j-1]], nums[arr[i+num2][j-1]])
                if nums[arr[i][j-1]]<=nums[arr[i+num2][j-1]]:
                    arr[i][j] = arr[i][j-1]
                else:
                    arr[i][j] = arr[i+num2][j-1]
                # arr[i][j] = min(nums[arr[i][j-1]], nums[arr[i+num2][j-1]])




    return arr



def query(i, j, lookup, nums):
    l = j - i +1
    k = int(math.log(l, 2))
    num = 2**k
    num1 = nums[lookup[i][k]]
    if l - k == 0:
        return nums[num1]
    
    num2 = nums[lookup[i+l-2**k][k]]
    return min(num1, num2)







arr = [7, 2, 3, 0, 5, 10, 3, 12, 18]

n = len(arr)

lookup = [[None for _ in range(int(math.log(n, 2))+1)] for _ in range(n)]
# print(lookup)


lookup = createTable(lookup, n, arr)

# print(lookup)
start = time.time()
print(query(7, 8, lookup, arr))
