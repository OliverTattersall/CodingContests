from itertools import permutations 


# lst = ["1", "2", "3"]
lst = [i for i in range(3)]

#returns a list of tuples containing n items, where n is length of original list or string
def permutiter(lst):
    return set(permutations(list(lst)))

# print(permutiter("AABBBBBBBBBBBBBBB"))

permuts=[]

#only works on strings. returns list of string permutations
def permutationsNoIter(lst, head, tail=""):
    if len(head) == 0:
        lst.append(tail)
    else:
        for i in range(len(head)):
            permutationsNoIter(permuts, head[:i] + head[i+1:], tail + head[i])

# permutationsNoIter(permuts, lst)
print(permuts)

#returns 2d list with each permutation being broken up into lists. applies yield, which can be used to add create generator objects. 
def all_perms(elements, lst2 = []):

    if len(elements) <=1:
        # lst.append(elements)
        return [elements]
        # yield elements
    else:

        for perm in all_perms(elements[1:]):

            # print(perm, elements)
            for i in range(len(elements)):
                lst2.append(perm[:i]+elements[0:1]+perm[i:])
                # print(perm[:i] + elements[0:1]+perm[i:])
                # yield perm[:i] + elements[0:1] + perm[i:]
        return lst2

print(list(all_perms(lst, [])))
