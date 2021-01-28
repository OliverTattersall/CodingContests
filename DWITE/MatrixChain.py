def matrixChainMin(matrices, i, j, lookup1):
    if i+1>=j:
        return 0
    key=(i, j)
    low = float("inf")

    if key not in lookup1:

        for k in range(i+1, j):

            cost=matrixChainMin(matrices, i, k, lookup1) + matrixChainMin(matrices, k, j, lookup1) + matrices[i]*matrices[k]*matrices[j]
            
            if cost<low:
                low=cost
        lookup1[key]=low
    return lookup1[key]




def matrixChainMax(matrices, i, j, lookup2):
    if i+1>=j:
        return 0
    key=(i, j)
    high = float("-inf")

    if key not in lookup2:

        for k in range(i+1, j):

            cost=matrixChainMax(matrices, i, k, lookup2) + matrixChainMax(matrices, k, j, lookup2) + matrices[i]*matrices[k]*matrices[j]
            
            if cost>high:
                high=cost
        lookup2[key]=high
    return lookup2[key]


matrices=input().split()[:-1]
for i in range(len(matrices)):
    matrices[i]=int(matrices[i])

lookup1=dict()
lookup2=dict()
l=len(matrices)

print(matrixChainMin(matrices, 0, l-1, lookup1), matrixChainMax(matrices, 0, l-1, lookup2))