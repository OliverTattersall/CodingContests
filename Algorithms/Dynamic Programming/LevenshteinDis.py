def LevDistance(T, a, b):
    
    for i in range(len(b)+1):
        T[i][0]=i
    for i in range(len(a)+1):
        T[0][i]=i

    for i in range(1, len(b)+1):
        for j in range(1, len(a)+1):
            temp=min(T[i-1][j], T[i-1][j-1], T[i][j-1])
            if a[j-1]==b[i-1]:
                T[i][j]=temp
            else:
                T[i][j]=temp+1

    return T[-1][-1]








word1=input()
word2=input()
T=[[0 for _ in range(len(word1)+1)] for _ in range(len(word2)+1)]

print(LevDistance(T, word1, word2))