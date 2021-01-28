# def LCS(X, Y, m, n, T):
 
#     # return empty string if we have reached the end of
#     # either sequence
#     if m == 0 or n == 0:
#         return str()
 
#     # if last character of X and Y matches
#     if X[m - 1] == Y[n - 1]:
#         # append current character (X[m-1] or Y[n-1]) to LCS of
#         # substring X[0..m-2] and Y[0..n-2]
#         return LCS(X, Y, m - 1, n - 1, T) + X[m - 1]
 
#     # else when the last character of X and Y are different
 
#     # if top cell of current cell has more value than the left
#     # cell, then drop current character of X and find LCS
#     # of substring X[0..m-2], Y[0..n-1]
 
#     if T[m - 1][n] > T[m][n - 1]:
#         return LCS(X, Y, m - 1, n, T)
#     else:
#         # if left cell of current cell has more value than the top
#         # cell, then drop current character of Y and find LCS
#         # of substring X[0..m-1], Y[0..n-2]
#         return LCS(X, Y, m, n - 1, T)
 
 
# # Function to fill lookup table by finding the length of LCS
# # of substring X[0..m-1] and Y[0..n-1]
# def LCSLength(X, Y, m, n, T):
 
#     # fill the lookup table in bottom-up manner
#     for i in range(1, m + 1):
#         for j in range(1, n + 1):
#             # if current character of X and Y matches
#             if X[i - 1] == Y[j - 1]:
#                 T[i][j] = T[i - 1][j - 1] + 1
#             # else if current character of X and Y don't match
#             else:
#                 T[i][j] = max(T[i - 1][j], T[i][j - 1])
 
 
# if __name__ == '__main__':
 
#     X = "XMJYAUZ"
#     Y = "MZJAWXU"
 
#     m = len(X)
#     n = len(Y)
 
#     # T[i][j] stores the length of LCS of substring X[0..i-1], Y[0..j-1]
#     T = [[0 for x in range(n + 1)] for y in range(m + 1)]
 
#     # fill lookup table
#     LCSLength(X, Y, m, n, T)
#     print(T)
#     # find longest common sequence
#     print(LCS(X, Y, m, n, T))


##################################################################
# Finding all LCS's 
#
##################################################################


def LCS(X, Y, m, n, T):
 
    # if we have reached the end of either sequence
    if m == 0 or n == 0:
        # create a List with 1 empty string and return
        return [""]
    
    # if last character of X and Y matches
    if X[m - 1] == Y[n - 1]:
 
        # ignore last characters of X and Y and find all LCS of substring
        # X[0..m-2], Y[0..n-2] and store it in a List
        lcs = LCS(X, Y, m - 1, n - 1, T)
 
        # append current character X[m - 1] or Y[n - 1]
        # to all LCS of substring X[0..m-2] and Y[0..n-2]

        lcs=[l + X[m - 1] for l in lcs]
        # for i in range(len(lcs)):
        #     lcs[i] = lcs[i] + (X[m - 1])
 
        return lcs
 
    # we reach here when the last character of X and Y don't match
 
    # if top cell of current cell has more value than the left cell,
    # then ignore current character of X and find all LCS of
    # substring X[0..m-2], Y[0..n-1]
    if T[m - 1][n] > T[m][n - 1]:
        return LCS(X, Y, m - 1, n, T)
 
    # if left cell of current cell has more value than the top cell,
    # then ignore current character of Y and find all LCS of
    # substring X[0..m-1], Y[0..n-2]
    if T[m][n - 1] > T[m - 1][n]:
        return LCS(X, Y, m, n - 1, T)
 
    # if top cell has equal value to the left cell, then consider both character
 
    top = LCS(X, Y, m - 1, n, T)
    left = LCS(X, Y, m, n - 1, T)
 
    # merge two Lists and return
    return top + left
 
 
# Function to fill lookup table by finding the length of LCS
# of substring X and Y
def LCSLength(X, Y, T):
 
    # fill the lookup table in bottom-up manner
    for i in range(1, len(X) + 1):
        for j in range(1, len(Y) + 1):
            # if current character of X and Y matches
            if X[i - 1] == Y[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
 
            # else if current character of X and Y don't match
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
 
 
# Function to find all LCS of X[0..m-1] and Y[0..n-1]
def findLCS(X, Y, T):
 
    # fill lookup table
    LCSLength(X, Y, T)
 
    # find all longest common sequences
    lcs = LCS(X, Y, len(X), len(Y), T)
 
    # since List can contain duplicates, "convert" the List to Set
    # and return
    return set(lcs)
 
 
if __name__ == '__main__':
 
    X = "ABDCAB"
    Y = "ABBCD"
 
    # T[i][j] stores the length of LCS of substring X[0..i-1], Y[0..j-1]
    T = [[0 for x in range(len(Y) + 1)] for y in range(len(X) + 1)]
 
    lcs = findLCS(X, Y, T)
    print(lcs)
    print(T)