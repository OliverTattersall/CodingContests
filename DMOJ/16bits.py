times=int(input())
options=[]
for i in range(times):
    options.append(input().split())

# print(options)

for i in range(len(options)):
    if int(options[i][0])*int(options[i][1]) == int(options[i][2]):
        print("POSSIBLE DOUBLE SIGMA")
    else:
        print("16 BIT S/W ONLY")