#mine
def MatrixChain(matrices, i, j, lookup):
    if i+1>=j:
        return 0
    key=(i, j)

    if key not in lookup:
        low = float("inf")

        for k in range(i+1, j):

            cost = MatrixChain(matrices, i, k, lookup)
            cost += MatrixChain(matrices, k, j, lookup)

            cost += matrices[i]*matrices[k]*matrices[j]

            if cost<low:
                low=cost

        lookup[key]=low

    return lookup[key]




matrices=input().split()[:-1]
for i in range(len(matrices)):
    matrices[i]=int(matrices[i])
lookup=dict()
print(MatrixChain(matrices, 0, len(matrices)-1, lookup))

