import math

def findFactors(n):
    factors=set([]) #creates a set named factors. when adding an item to a set, if it is already in there, it will not add a duplicate
    #loop from 1 to √n+1 as √n is the highest factor possible, taking the lower factor of a pair. ex. 36: (1,36),(2,18),(3,12),(4,9),(6,6) 6 is the highest factor out of the lower factor in a pair and 6 is the √36
    for i in range(1,int( math.sqrt(n))+1, 1):
        if n%i==0:
            factors.add(i)
            factors.add((n//i))

    factors=list(factors)
    factors.sort()
    return factors

'''
This Function finds the first triangle number with more than 500 factors
Paramters: Integer n
Conditions: n>0
'''

def EulerProblem12(n):
    test=False
    triangles=[1]
    while test==False:
        if len(findFactors(triangles[-1]))>=n:
            test=True
            return triangles[-1]
        else:
            # adds the next triangle number
            triangles.append((len(triangles)+1)**2-triangles[len(triangles)-1])
    
print(EulerProblem12(500))
# print(EulerProblem12(20))
# print(EulerProblem12(1))

