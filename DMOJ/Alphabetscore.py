word = input()

letters={}
alphabet = list("abcdefghijklmnopqrstuvwxyz")
sum = 0

for i in word:
    letters[i] = letters.get(i, 0)+1

for i in range(len(alphabet)):
    if alphabet[i] in letters:
        sum+= letters[alphabet[i]]*(i+1)

print(sum)
