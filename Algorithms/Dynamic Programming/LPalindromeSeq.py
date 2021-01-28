# Function to find length of LCS of substring X[0..n-1] and Y[0..n-1]
def PalindromeLength(X, Y, n, T):

    # first row and first column of the lookup table
    # are already 0 as T is globally declared

    # fill the lookup table in bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # if current character of X and Y matches
            if X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1

            # else if current character of X and Y don't match
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])

    return T


# Function to find LCS of X[0..m-1] and Y[0..n-1]
def longestPalindrome(X, Y, m, n, T):

    # return empty string if we have reached the end of
    # either sequence
    if m == 0 or n == 0:
        return ""

    # if last character of X and Y matches
    if X[m - 1] == Y[n - 1]:

        # append current character (X[m-1] or Y[n-1]) to LCS of
        # substring X[0..m-2] and Y[0..n-2]
        return longestPalindrome(X, Y, m - 1, n - 1, T) + X[m - 1]

    # else when the last character of X and Y are different

    # if top cell of current cell has more value than the left
    # cell, then drop current character of X and find LCS
    # of substring X[0..m-2], Y[0..n-1]

    if T[m - 1][n] > T[m][n - 1]:
        return longestPalindrome(X, Y, m - 1, n, T)

    # if left cell of current cell has more value than the top
    # cell, then drop current character of Y and find LCS
    # of substring X[0..m-1], Y[0..n-2]

    return longestPalindrome(X, Y, m, n - 1, T)




X = "ABBDCACBD"

# Y is reverse of X
Y = X[::-1]

# T[i][j] stores the length of LCS of substring X[0..i-1], Y[0..j-1]
T = [[0 for x in range(len(X) + 1)] for y in range(len(X) + 1)]
T=PalindromeLength(X, Y, len(X), T)


# Print Longest Palindromic Subsequence using lookup table
print("The Longest Palindromic Subsequence is", longestPalindrome(X, Y, len(X), len(X), T))

#find all palindromic sequences - doesnt work
def findPalindromes(X, Y, m, n, T):

    if m==0 or n==0:
        return [""]
    

    if X[m-1] == Y[n-1]:
        lps=findPalindromes(X, Y, m-1, n-1, T)

        lps=[s + X[m-1] for s in lps]
        
        return lps

    if T[m-1][n] > T[m][n-1]:

        return findPalindromes(X, Y, m - 1, n, T)

    if T[m-1][n] < T[m][n-1]:

        return findPalindromes(X, Y, m , n - 1, T)

    top=findPalindromes(X, Y, m - 1, n, T)
    left=findPalindromes(X, Y, m, n - 1, T)

    return top + left



print(T)
lps=findPalindromes(X, Y, len(X), len(Y), T)
print(set(lps))
