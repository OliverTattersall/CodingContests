'''
This function finds the difference between ((1+2..+n)^2)-(1^2+2^2...+n^2)
Parameters: Integer n
Conditions: n>0
'''
def EulerProblem6(n):
    sum1=0
    sum2=sum([i for i in range(1, n+1)])**2
    for i in range(1, n+1):
        sum1+=i**2
    return sum2-sum1

def EulerProblem6p2(n):
    sum1 = n*(n+1)*(2*n+1)//6
    sum2 = (n*(n+1)//2)**2
    return sum2-sum1

# print(EulerProblem6(10))
# print(EulerProblem6(100))
print(EulerProblem6p2(100))