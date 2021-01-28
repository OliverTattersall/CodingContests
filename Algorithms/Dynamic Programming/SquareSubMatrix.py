
def largestSquare(M):
    max=0
    T=[[0 for _ in range(len(M[0])+1)] for _ in range(len(M)+1)]

    for i in range(1, len(M)+1):
        for j in range(1, len(M[0])+1):
            if M[i-1][j-1]=="0":
                T[i][j]=0

            else:
                T[i][j]=min( T[i-1][j-1], T[i][j-1], T[i-1][j] )+1
                if T[i][j]>max:
                    max=T[i][j]

    return max


M=[]
for i in range(8):
    M.append(input().split())

print(largestSquare(M))


