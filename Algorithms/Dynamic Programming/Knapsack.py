import time



N=int(input())
knapweight=int(input())
objects=[]
for i in range(N):
    item=input().split()
    objects.append([int(item[0]), int(item[1])])

objects.sort(key=lambda x:x[1])

print(objects)

start_time1 = time.time()

T=[[0 for _ in range(knapweight+1)] for _ in range(N)]

# print(T)

for i in range(N):
    for j in range(len(T[i])):
        if i==0:
            if objects[i][1]<=j:
                T[i][j]=objects[i][0]
        else:
            if objects[i][1]>j:
                T[i][j]=T[i-1][j]
            else:
                T[i][j]=max(objects[i][0]+T[i-1][j-objects[i][1]] ,T[i-1][j])
    
# print(T)
# print(T[-1][-1])
            

print("--- %s seconds ---" % (time.time() - start_time1))
print(T[-1][-1])


######################
#
# recursive online way
#
######################


##O(2^n)
def knapSack(W , wt , val , n): 
  
    # Base Case 
    if n == 0 or W == 0: 
        return 0
  
    # If weight of the nth item is more than Knapsack of capacity 
    # W, then this item cannot be included in the optimal solution 
    if (wt[n-1] > W): 
        return knapSack(W , wt , val , n-1) 
  
    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included 
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1),  knapSack(W , wt , val , n-1)) 
  
start_time2 = time.time()

val = [objects[i][0] for i in range(len(objects))] 
wt = [objects[i][1] for i in range(len(objects))]
W = 7
n = len(val) 
# print(knapSack(W , wt , val , n))

print("--- %s seconds ---" % (time.time() - start_time2))










#memoized way

def knapSackM(W, wt, val, n, lookup):
    if n==0 or W==0:
        return 0
    
    if W<0:
        return float("-inf")

    key =(n,W)
    if key not in lookup:
        inc = val[n-1] + knapSackM(W-wt[n-1], wt, val, n-1, lookup)
        exc = knapSackM(W, wt, val, n-1, lookup)
        lookup[key] = max(inc, exc)
    return lookup[key]

print(knapSackM(10, [1, 2, 3, 8, 7, 4], [20, 5, 10, 40, 15, 25], 6, {}))