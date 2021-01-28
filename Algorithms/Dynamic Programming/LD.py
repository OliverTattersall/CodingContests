#memoized version - me
def LD(X, Y, m, n, lookup):

    if m==0 or n==0:
        return m+n

    key=(m,n)

    if key not in lookup:

        if X[m-1] == Y[n-1]:
            lookup[key]= LD(X, Y, m-1, n-1, lookup)
        else:
            lookup[key]= min(LD(X, Y, m, n-1, lookup)+1, LD(X, Y, m-1, n, lookup)+1, LD(X, Y, m-1, n-1, lookup)+1)

    return lookup[key]


X="kitten"
Y="sitting"
lookup={}
answer=LD(X, Y, len(X), len(Y), lookup)
print(answer)


#Tabulated version - me

def LDlength(X, Y, m, n):

    T=[[0 for _ in range(m+1)] for _ in range(n+1)]

    for i in range(m+1):
        T[0][i]=i

    for i in range(n+1):
        T[i][0]=i



    for i in range(1, n+1):
        for j in range(1, m+1):
            if X[j-1]==Y[i-1]:
                T[i][j]=T[i-1][j-1]

            else:

                T[i][j]=min(T[i-1][j-1], T[i-1][j], T[i][j-1])+1


    return T[-1][-1]


print(LDlength(X, Y, len(X), len(Y)))

    