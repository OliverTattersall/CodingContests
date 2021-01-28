alpha=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#vowels=[{'vowel':'a','value':0},{"vowel":"e","value":4},{"vowel":"i", "value":8},{"vowel":"o","value":14},{"vowel":"u","value":20}]

starter=input()
outputstr=""

for i in range(len(starter)):
    value=0
    if starter[i]=="a" or starter[i]=="e" or starter[i]=="i" or starter[i]=="o" or starter[i]=="u":
        outputstr+=starter[i]
    else:
        for j in range(26):
            if starter[i]==alpha[j]:
                value = j
                break
                
        outputstr+=starter[i]
        if value<3:
            outputstr+="a"
        elif value>2 and value<7:
            outputstr+="e"
        elif value>6 and value<12:
            outputstr+="i"
        elif value>11 and value<18:
            outputstr+="o"
        elif value>17:
            outputstr+="u"
        if value==25:
            outputstr+="z"
        elif value==3 or value==7 or value==13 or value==19:
            outputstr+=alpha[value+2]
        else:
            outputstr+=alpha[value+1]
        
print(outputstr)