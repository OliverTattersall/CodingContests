#memoized version of smallest super sequence - top down - I made it

def SCS(X, Y, m, n, lookup):

    if m==0 or n==0:
        return n+m

    key=(m,n)

    if key not in lookup:

        if X[m-1]==Y[n-1]:
            lookup[key]= SCS(X, Y, m-1, n-1, lookup)+1

        else:
            lookup[key]= min(SCS(X, Y, m, n-1, lookup)+1, SCS(X, Y, m-1, n, lookup)+1)

    return lookup[key]



X="ABCBDAB"
Y="BDCABA"
lookup={}

print(SCS(X, Y, len(X), len(Y), lookup))




#Tabulated version - bottom up - Online version
# Function to find length of shortest Common supersequence of
# sequences X[0..m-1] and Y[0..n-1]
def SCSLength(X, Y):
 
    m = len(X)
    n = len(Y)
 
    # lookup table stores solution to already computed sub-problems
    # i.e. T[i][j] stores the length of SCS of substring
    # X[0..i-1] and Y[0..j-1]
    T = [[0 for x in range(n + 1)] for y in range(m + 1)]
    
 
    # initialize first column of the lookup table
    for i in range(m + 1):
        T[i][0] = i
 
    # initialize first row of the lookup table
    for j in range(n + 1):
        T[0][j] = j
        
    print(T)
    # fill the lookup table in bottom-up manner
    for i in range(1, m + 1):
        for j in range(1, n + 1):
 
            # if current character of X and Y matches
            if X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
 
            # else if current character of X and Y don't match
            else:
                T[i][j] = min(T[i - 1][j] + 1, T[i][j - 1] + 1)
 
    # SCS will be last entry in the lookup table
    return T
 
 


X = "ABCB"
Y = "BDC"

# print(SCSLength(X, Y))



#####################
#
# Finding all SCS's
#
####################

    

def findSCS(X, Y, m, n, T):
    
    if n==0:
        return [X[:m]]
    if m==0:
        return [Y[:n]]

    if X[m-1]==Y[n-1]:

        scs=findSCS(X,Y, m-1, n-1, T)
        return [s+X[m-1] for s in scs]
        

    if T[m-1][n]<T[m][n-1]:

        scs=findSCS(X, Y, m - 1, n, T)
        
        return [s + X[m-1] for s in scs]

    if T[m-1][n]>T[m][n-1]:
        scs=findSCS(X, Y, m, n-1, T)
        return [s + Y[n-1] for s in scs]

    
    top = findSCS(X, Y, m - 1, n, T)
    left = findSCS(X, Y, m, n - 1, T)

    return [s + X[m - 1] for s in top] + [s + Y[n - 1] for s in left]
    
    


X = "ABCBDAB"
Y = "BDCABA"

T=SCSLength(X, Y)
print(T)
A=set(findSCS(X, Y, len(X), len(Y), T))

print(A)