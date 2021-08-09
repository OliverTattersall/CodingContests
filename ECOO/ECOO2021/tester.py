from itertools import permutations 

lst = [i for i in range(3)]

def permutiter(lst):
    return list(permutations(list(lst)))

x = permutiter(lst)
opt=set()
for i in range(len(x)):
    opt.add(x[i])

print(opt)