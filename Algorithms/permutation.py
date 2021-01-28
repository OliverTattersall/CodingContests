from itertools import permutations 


# word=input()

# def permutiter(word):
#     return list(permutations(list(word)))

# print(permutiter(word))

permuts=[]
def permutationsNoIter(lst, head, tail=""):
    if len(head) == 0:
        lst.append(tail)
    else:
        for i in range(len(head)):
            permutationsNoIter(permuts, head[:i] + head[i+1:], tail + head[i])

permutationsNoIter(permuts, ['1','2','3', '4'])
print(permuts)