#my function

def findChange(coins, goal):

    T=[[0 for _ in range(goal+1)] for _ in range(len(coins)+1)]

    # for i in range(goal+1):
    #     T[0][i]=float("inf")

    for i in range(1, len(coins)+1):
        for j in range(1, goal+1):
            if i==1:
                T[i][j]=j//coins[i-1]

            else:
            # print(j//coins[i-1]+ T[i-1][j%coins[i-1]], T[i-1][j])

                T[i][j]=min(j//coins[i-1]+T[i-1][j%coins[i-1]], T[i-1][j])

    return T


coins=[1, 3, 5, 7]

goal=15

print(findChange(coins, goal))