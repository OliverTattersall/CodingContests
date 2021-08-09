'''
This Function finds the largest palindrome that is the product of 2 n-digit factors. 
Parameter: Integer n
Conditions: n>0
'''

def EulerProblem4(n):
    highestproduct=int("9"*n)**2

    for i in range(highestproduct, 0, -1):
        if str(i)==str(i)[::-1]:
            # print(i)
            for j in range(i,10**(n-1), -1):
                if i%j==0:
                    if len(str(j))==n and len(str(i//j))==n:
                        return j*(i//j)

            
print(EulerProblem4(2))
print(EulerProblem4(3))
