
def findPath(M):
    T=[[0 for _ in range(len(M[0])+1)] for _ in range(len(M)+1)]

    for i in range( len(M[0])):
        T[1][i+1]=M[0][i]+T[1][i]

    for i in range(len(M)):
        T[i+1][1]=M[i][0]+T[i][1]

    # print(T)

    for i in range(2, len(M)+1):
        for j in range(2, len(M[0])+1):
            T[i][j]=min(T[i-1][j], T[i][j-1])+M[i-1][j-1]

    return T[-1][-1]




Matrix=[
        [4, 7, 8, 6, 4],
        [6, 7, 3, 9, 2],
        [3, 8, 1, 2, 4],
        [7, 1, 7, 3, 7],
        [2, 9, 8, 9, 3]
    ]

print(findPath(Matrix))