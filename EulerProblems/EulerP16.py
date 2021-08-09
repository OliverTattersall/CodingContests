'''
This function finds the sum of the digits of the number 2^n
Parameters: Integer n
'''

def EulerProblem16(n):
    num=2**n
    num=str(num)
    num=num.replace(".", "")
    sum=0
    for i in range(len(num)):
        sum=sum+int(num[i])

    return sum
    
# print(EulerProblem16(0))
# print(EulerProblem16(15))
print(EulerProblem16(1000))
# print(EulerProblem16(-2))