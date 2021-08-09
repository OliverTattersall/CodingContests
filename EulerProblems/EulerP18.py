tri = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

tri=tri.split("\n")
for i in range(len(tri)):
    tri[i]=list(map(int, tri[i].split()))
# print(tri)


#top down
def triangle(tri, i, j):
    if i==len(tri)-1:

        return tri[i][j]

    left = triangle(tri, i+1, j)+tri[i][j]
    right = triangle(tri, i+1, j+1)+tri[i][j]

    return max(left, right)


print(triangle(tri, 0, 0))


tri2 = list(map( lambda x:list(map(lambda y:0, x)),tri.copy()))
tri2[-1]=tri[-1]
# print(tri2)
#bottom up
def solve(tri):
    for i in range(len(tri)-1, 0, -1):
        for k in range(len(tri2[i])-1):
            tri2[i-1][k] = tri[i-1][k]+max(tri2[i][k], tri2[i][k+1])
    return tri2[0][0]
print(solve(tri))