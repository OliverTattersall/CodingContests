# Function to find length of Longest Common Subsequence of substring
# X[0..m-1] and Y[0..n-1]
def LCSLength(X, Y, m, n, lookup):
    # return if we have reached the end of either string
    if m == 0 or n == 0:
        return 0
 
    # construct a unique dict key from dynamic elements of the input
    key = (m, n)
 
    # if sub-problem is seen for the first time, solve it and
    # store its result in a dict
    if key not in lookup:
 
        # if last character of X and Y matches
        if X[m - 1] == Y[n - 1]:
            lookup[key] = LCSLength(X, Y, m - 1, n - 1, lookup) + 1
 
        else:
            # else if last character of X and Y don't match
            lookup[key] = max(LCSLength(X, Y, m, n - 1, lookup),
                              LCSLength(X, Y, m - 1, n, lookup))
 
    # return the sub-problem solution from the dictionary
    return lookup[key]
 
 
 
X = "ABCBDAB"
Y = "BDCABA"

# create a dictionary to store solutions of subproblems
lookup = {}

print("The length of LCS is", LCSLength(X, Y, len(X), len(Y), lookup))
print(lookup)


print(max({1:2, 3:4, 2:6}))