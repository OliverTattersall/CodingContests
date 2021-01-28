# Function to find LRS of substrings X[0..m-1], X[0..n-1]
def LRS(X, m, n, T):
 
    # if we have reached the end of either sequence
    # return empty string
    if m == 0 or n == 0:
        return ""
 
    # if characters at index m and n matches and index is different
    if X[m - 1] == X[n - 1] and m != n:
        return LRS(X, m - 1, n - 1, T) + X[m - 1]
    else:
        # else if characters at index m and n don't match
        if T[m - 1][n] > T[m][n - 1]:
            return LRS(X, m - 1, n, T)
        else:
            return LRS(X, m, n - 1, T)
 
 
# Function to fill lookup table by finding the length of LRS
# of substring X[0..n-1]
def LRSLength(X, T):
 
    # first row and first column of the lookup table
    # are already 0 as T is globally declared
 
    # fill the lookup table in bottom-up manner
    for i in range(1, len(X) + 1):
        for j in range(1, len(X) + 1):
            # if characters at index i and j matches
            # and the index is different
            if X[i - 1] == X[j - 1] and i != j:
                T[i][j] = T[i - 1][j - 1] + 1
            # else if characters at index i and j are different
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
 
 

 
X = "ATACTCGGA"

# T[i][j] stores the length of LRS of substring X[0..i-1], X[0..j-1]
T = [[0 for x in range(len(X) + 1)] for y in range(len(X) + 1)]

# fill lookup table
LRSLength(X, T)

# find Longest Repeating Subsequence
print(LRS(X, len(X), len(X), T))