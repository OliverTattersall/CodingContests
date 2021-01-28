#function that finds the longest palindromic substring
def LongestPalindrome(X, Y, n):

    maxLength = 0              
    endingIndex = n 

    T=[[0 for _ in range(n+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, n+1):
            if X[i-1]==Y[j-1]:
                T[i][j]=T[i-1][j-1]+1

                if T[i][j] > maxLength:
                    maxLength = T[i][j]
                    endingIndex = i

    return T, X[endingIndex - maxLength: endingIndex]









X="ABADCACB"
Y=X[::-1]
print(Y)

T=LongestPalindrome(X, Y, len(X))
print(T)