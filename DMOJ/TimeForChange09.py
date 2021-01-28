answers=[]
tables=[]
for k in range(5):
    goal=int(input())
    nums=int(input())
    coins=[]
    combos=[]
    for i in range(nums):
        coins.append(int(input()))
    coins.sort()

    table=[[0 for _ in range(goal+1)] for _ in range(len(coins)+1)]

    for i in range(1, len(coins)+1):
        for j in range(1, goal+1):
            if i==1:
                if j//coins[i-1]==j/coins[i-1]:
                    table[i][j]=j//coins[i-1]
                else:
                    table[i][j]=float("inf")
                

            else:
                # print(i, j, coins[i])
                item1=j//coins[i-1]+table[i-1][j%coins[i-1]]
                item2=table[i-1][j]
                table[i][j]=min(item1, item2)

    answers.append(table[-1][-1])
    # tables.append(table)

for i in range(5):
    print(answers[i])
    # print(tables[i])


