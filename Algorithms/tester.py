

x = "ABCBDAB"
y = "BDCABA"

def findLCS(x,y):
    T = [[0 for _ in range(len(x)+1)] for _ in range(len(y)+1)]
    
    for i in range(1, len(y)+1):
        for j in range(1, len(x)+1):
            if x[j-1] == y[i-1]:
                T[i][j] = T[i-1][j-1]+1
            else:
                T[i][j] = max(T[i-1][j-1], T[i-1][j], T[i][j-1])
    print(T)

    return T[len(y)][len(x)]

print(findLCS(x,y))
