import re
# n = int(input())
# test = ''
# for i in range(n):
#     test+=input()+"\n"
test = '''Before 02/03/04, but not after December 19, 99,
there was a rehash of the 55.34.02 meeting. A date, like November 15,
95 cannot traverse two lines, nor can it be surrounded by alphabetics
or numerics like this: 78November 01, 88, or 6801/12/03, or 02/03/04x.'''

groups = re.findall("[,.\s][0-9][0-9][./][0-1][0-9][./][0-3][0-9][,.\s]", test)
spaces = re.split("[,.\s][0-9][0-9][./][0-1][0-9][./][0-3][0-9][,.\s]", test)
print(groups)
end = ''
last = 0

