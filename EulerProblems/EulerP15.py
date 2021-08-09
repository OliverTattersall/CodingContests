'''
This functions finds the total possible paths created by a n*n square
Parameters: Integer n
Conditions: n>0
'''
def EulerProblem15(n):
    lst=[[1 for i in range(n+1)]for i in range(n+1)] # creates 2-dimensional array with n+1 by n+1 dimensions, initialized with integer 1
    for i in range(1, n+1, 1):
        for j in range(1, n+1, 1):
            lst[i][j]=lst[i-1][j]+lst[i][j-1]

    return lst[-1][-1]
            
print(EulerProblem15(20))