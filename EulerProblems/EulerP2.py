'''
Function finds sum of all even fibonacci numbers between 0 and n
Parameters: Integer n
Conditions n>=2
'''

def EulerProblem2(n):
    fib=[1,1] 
    sum=0
    while fib[-1]<n:
        newval=fib[-1]+fib[-2]
        if newval%2==0:
            sum+=newval
        fib.append(newval)
    return sum

# test case
print(EulerProblem2(4000000))
# print(2)