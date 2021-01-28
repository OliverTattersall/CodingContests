import sys
sys.setrecursionlimit(1500)

width=int(input())
height=int(input())
Matrix=[]
for i in range(width):
    Matrix.append(input().split(" "))

# print(Matrix)

# Matrix=[['3', '10', '8', '14'], ['1', '11', '4', '4'], ['6', '2', '12', '9']]

def go(m, n, lookup, count):
    if m==1 and n==1:
        return True

    if count==1499:
        return False

    for i in range(len(Matrix)):

        for j in range(len(Matrix[0])):
            # print(m*n)
            if Matrix[i][j]==str(m*n):
                # print(i, j)
                return go(i+1, j+1, lookup, count+1)


lookup={}
answer=go(len(Matrix), len(Matrix[0]), lookup, 0)

if answer:
    print("yes")
else:
    print("no")

